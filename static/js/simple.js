// Simple portfolio page JavaScript
document.addEventListener('DOMContentLoaded', function() {
    const modal = document.getElementById('contentModal');
    const modalClose = document.getElementById('modalClose');
    const modalTitle = document.getElementById('modalTitle');
    const modalBody = document.getElementById('modalBody');

    // Category mapping
    const categories = {
        'about': 'about_me',
        'education': 'education',
        'experience': 'experience',
        'projects': 'projects',
        'leadership': 'leadership',
        'extracurriculars': 'extracurriculars',
        'hobbies': 'hobbies'
    };

    // Load all cards for each category
    Object.keys(categories).forEach(categoryId => {
        loadCategoryCards(categoryId, categories[categoryId]);
    });

    // Close modal handlers
    modalClose.addEventListener('click', closeModal);
    modal.addEventListener('click', function(e) {
        if (e.target === modal) {
            closeModal();
        }
    });

    // Close modal on Escape key
    document.addEventListener('keydown', function(e) {
        if (e.key === 'Escape' && modal.classList.contains('active')) {
            closeModal();
        }
    });

    async function loadCategoryCards(categoryId, categoryPath) {
        try {
            const response = await fetch(`/api/category/${categoryPath}`);
            if (!response.ok) {
                console.error(`Failed to load ${categoryPath}`);
                return;
            }

            const data = await response.json();
            const cardsContainer = document.getElementById(`${categoryId}-cards`);

            if (!cardsContainer || !data.files || data.files.length === 0) {
                // Hide the entire section if no files
                const section = document.getElementById(categoryId);
                if (section) {
                    section.style.display = 'none';
                }
                return;
            }

            // Filter out Outlook.md from about_me section
            let filesToShow = data.files;
            if (categoryPath === 'about_me') {
                filesToShow = data.files.filter(file => 
                    !file.filename.toLowerCase().includes('outlook')
                );
            }

            // Hide section if no files after filtering
            if (filesToShow.length === 0) {
                const section = document.getElementById(categoryId);
                if (section) {
                    section.style.display = 'none';
                }
                return;
            }

            // Create cards for each file
            filesToShow.forEach(file => {
                const card = createCard(file, categoryPath);
                cardsContainer.appendChild(card);
            });
        } catch (error) {
            console.error(`Error loading ${categoryPath}:`, error);
        }
    }

    function createCard(file, categoryPath) {
        const card = document.createElement('div');
        card.className = 'card';
        
        const title = document.createElement('div');
        title.className = 'card-title';
        title.textContent = file.displayName;

        const preview = document.createElement('div');
        preview.className = 'card-preview';
        preview.textContent = file.preview || 'Click to view details...';

        card.appendChild(title);
        card.appendChild(preview);

        // Add click handler
        card.addEventListener('click', () => {
            openModal(file.filename, categoryPath, file.displayName);
        });

        return card;
    }

    async function openModal(filename, categoryPath, displayName) {
        try {
            modalTitle.textContent = displayName;
            modalBody.innerHTML = '<div style="text-align: center; padding: 2rem;">Loading...</div>';
            modal.classList.add('active');
            document.body.style.overflow = 'hidden';

            const response = await fetch(`/api/content/${categoryPath}/${filename}`);
            if (!response.ok) {
                throw new Error('Failed to load content');
            }

            const data = await response.json();
            modalBody.innerHTML = convertMarkdownToHTML(data.content);
        } catch (error) {
            console.error('Error loading content:', error);
            modalBody.innerHTML = '<p style="color: #e53e3e;">Error loading content. Please try again.</p>';
        }
    }

    function closeModal() {
        modal.classList.remove('active');
        document.body.style.overflow = '';
        modalTitle.textContent = '';
        modalBody.innerHTML = '';
    }

    function convertMarkdownToHTML(markdown) {
        // Simple markdown to HTML converter
        let html = markdown;

        // Code blocks first (to avoid processing inside them)
        html = html.replace(/```([\s\S]*?)```/gim, '<pre><code>$1</code></pre>');
        html = html.replace(/`([^`]+)`/gim, '<code>$1</code>');

        // Headers (order matters - most specific first)
        html = html.replace(/^#### (.*$)/gim, '<h4>$1</h4>');
        html = html.replace(/^### (.*$)/gim, '<h3>$1</h3>');
        html = html.replace(/^## (.*$)/gim, '<h2>$1</h2>');
        html = html.replace(/^# (.*$)/gim, '<h1>$1</h1>');

        // Bold (must come before italic to avoid conflicts)
        html = html.replace(/\*\*(.*?)\*\*/gim, '<strong>$1</strong>');
        html = html.replace(/__(.*?)__/gim, '<strong>$1</strong>');

        // Italic - match single asterisks/underscores (processed after bold)
        // Use word boundaries to avoid matching within words
        html = html.replace(/\*([^\*\n]+?)\*/gim, '<em>$1</em>');
        html = html.replace(/_([^_\n]+?)_/gim, '<em>$1</em>');

        // Lists - process line by line
        const lines = html.split('\n');
        const processedLines = [];
        let inList = false;

        for (let i = 0; i < lines.length; i++) {
            const line = lines[i];
            const listMatch = line.match(/^[\*\-\+] (.+)$/);
            
            if (listMatch) {
                if (!inList) {
                    processedLines.push('<ul>');
                    inList = true;
                }
                processedLines.push(`<li>${listMatch[1]}</li>`);
            } else {
                if (inList) {
                    processedLines.push('</ul>');
                    inList = false;
                }
                processedLines.push(line);
            }
        }
        
        if (inList) {
            processedLines.push('</ul>');
        }
        
        html = processedLines.join('\n');

        // Paragraphs (lines that aren't already HTML tags)
        html = html.split('\n').map(line => {
            const trimmed = line.trim();
            if (!trimmed) return '';
            if (trimmed.match(/^<[hul]/) || trimmed.match(/^<\/[hul]/) || 
                trimmed.match(/^<pre>/) || trimmed.match(/^<\/pre>/) ||
                trimmed.match(/^<code>/) || trimmed.match(/^<\/code>/) ||
                trimmed.match(/^<p>/) || trimmed.match(/^<\/p>/)) {
                return line;
            }
            return '<p>' + trimmed + '</p>';
        }).join('\n');

        // Clean up empty paragraphs and fix nested tags
        html = html.replace(/<p><\/p>/gim, '');
        html = html.replace(/<p>(<[hul])/gim, '$1');
        html = html.replace(/(<\/[hul]>)<\/p>/gim, '$1');
        html = html.replace(/<p>(<pre>)/gim, '$1');
        html = html.replace(/(<\/pre>)<\/p>/gim, '$1');

        // Clean up multiple empty lines
        html = html.replace(/\n{3,}/gim, '\n\n');

        return html;
    }
});
