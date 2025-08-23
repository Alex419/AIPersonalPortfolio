// Chat functionality for dystopian TV interface
class DystopianChatBot {
    constructor() {
        this.chatMessages = document.getElementById('chatMessages');
        this.chatInput = document.getElementById('chatInput');
        this.sendButton = document.getElementById('sendButton');
        this.welcomeMessage = document.getElementById('welcomeMessage');
        this.chatInterface = document.getElementById('chatInterface');
        this.isLoading = false;
        this.messageCount = 0;
        
        this.initializeEventListeners();
        this.initializeAtmosphere();
    }
    
    initializeEventListeners() {
        // Send message on button click
        this.sendButton.addEventListener('click', () => this.sendMessage());
        
        // Send message on Enter key
        this.chatInput.addEventListener('keypress', (e) => {
            if (e.key === 'Enter' && !e.shiftKey) {
                e.preventDefault();
                this.sendMessage();
            }
        });
        
        // Auto-resize input
        this.chatInput.addEventListener('input', () => {
            this.chatInput.style.height = 'auto';
            this.chatInput.style.height = this.chatInput.scrollHeight + 'px';
        });
        
        // Start chat when clicking on the input placeholder
        const inputPlaceholder = document.querySelector('.input-placeholder');
        if (inputPlaceholder) {
            inputPlaceholder.addEventListener('click', () => {
                this.startChat();
            });
        }
        
        // Also start chat on first input focus
        this.chatInput.addEventListener('focus', () => {
            if (this.messageCount === 0) {
                this.startChat();
            }
        });
    }
    
    initializeAtmosphere() {
        // Update timestamp
        this.updateTimestamp();
        setInterval(() => this.updateTimestamp(), 1000);
        
        // Add glitch effects
        this.addGlitchEffects();
        
        // Add scan line effect
        this.addScanLineEffect();
    }
    
    updateTimestamp() {
        const now = new Date();
        const timestamp = now.toLocaleString('en-US', {
            month: 'short',
            day: '2-digit',
            year: 'numeric',
            hour: '2-digit',
            minute: '2-digit',
            second: '2-digit',
            hour12: false
        });
        document.getElementById('timestamp').textContent = timestamp;
    }
    
    addGlitchEffects() {
        // Random glitch effects on the TV
        setInterval(() => {
            if (Math.random() < 0.1) { // 10% chance every interval
                this.tvGlitch();
            }
        }, 3000);
    }
    
    tvGlitch() {
        const tvScreen = document.querySelector('.tv-screen');
        tvScreen.style.filter = 'hue-rotate(90deg) saturate(2)';
        tvScreen.style.transform = 'skew(1deg, 0deg)';
        
        setTimeout(() => {
            tvScreen.style.filter = 'none';
            tvScreen.style.transform = 'none';
        }, 200);
    }
    
    addScanLineEffect() {
        const scanLines = document.querySelector('.scan-lines');
        setInterval(() => {
            scanLines.style.animation = 'none';
            setTimeout(() => {
                scanLines.style.animation = 'scanLineMove 0.1s linear';
            }, 10);
        }, 100);
    }
    
    startChat() {
        // Hide welcome message with glitch effect
        this.welcomeMessage.style.animation = 'glitchOut 0.5s ease-out forwards';
        
        setTimeout(() => {
            this.welcomeMessage.style.display = 'none';
            this.chatInterface.style.display = 'flex';
            this.chatInterface.style.animation = 'fadeIn 0.5s ease-out';
            
            // Focus on the input field
            this.chatInput.focus();
            
            // Add initial bot message
            this.addMessage("Neural link established. I'm Alex's digital echo. Ask me anything about my background, projects, or experience.", 'bot');
        }, 500);
    }
    
    async sendMessage() {
        const message = this.chatInput.value.trim();
        if (!message || this.isLoading) return;
        
        // Add user message to chat
        this.addMessage(message, 'user');
        this.chatInput.value = '';
        this.chatInput.style.height = 'auto';
        
        // Show loading indicator
        this.showLoading();
        
        try {
            // Send message to backend
            const response = await fetch('/chat', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ message: message })
            });
            
            const data = await response.json();
            
            if (response.ok) {
                // Add bot response
                this.addMessage(data.response, 'bot');
            } else {
                // Show error message
                this.addMessage(`System error: ${data.error}. Neural link may be unstable.`, 'bot');
            }
        } catch (error) {
            console.error('Error:', error);
            this.addMessage('Neural link disrupted. Please try again.', 'bot');
        } finally {
            this.hideLoading();
        }
    }
    
    addMessage(content, sender) {
        this.messageCount++;
        
        const messageDiv = document.createElement('div');
        messageDiv.className = `message ${sender}-message`;
        
        const avatar = document.createElement('div');
        avatar.className = 'message-avatar';
        
        const icon = document.createElement('i');
        if (sender === 'bot') {
            icon.className = 'fas fa-brain';
        } else {
            icon.className = 'fas fa-user';
        }
        
        avatar.appendChild(icon);
        
        const messageContent = document.createElement('div');
        messageContent.className = 'message-content';
        
        const paragraph = document.createElement('p');
        paragraph.textContent = content;
        messageContent.appendChild(paragraph);
        
        messageDiv.appendChild(avatar);
        messageDiv.appendChild(messageContent);
        
        this.chatMessages.appendChild(messageDiv);
        
        // Scroll to bottom
        this.scrollToBottom();
        
        // Add glitch animation for bot messages
        if (sender === 'bot') {
            setTimeout(() => {
                this.addGlitchToMessage(messageDiv);
            }, 100);
        }
        
        // Add message counter effect
        this.updateMessageCounter();
    }
    
    addGlitchToMessage(messageDiv) {
        // Random glitch effect
        if (Math.random() < 0.3) {
            messageDiv.style.animation = 'messageGlitch 0.1s ease-in-out';
            setTimeout(() => {
                messageDiv.style.animation = '';
            }, 100);
        }
    }
    
    updateMessageCounter() {
        const systemInfo = document.querySelector('.system-info');
        const messageCounter = systemInfo.querySelector('.message-counter') || 
            document.createElement('span');
        
        if (!messageCounter.classList.contains('message-counter')) {
            messageCounter.className = 'info-item message-counter';
            systemInfo.appendChild(messageCounter);
        }
        
        messageCounter.textContent = `MESSAGES: ${this.messageCount}`;
    }
    
    showLoading() {
        this.isLoading = true;
        this.sendButton.disabled = true;
        this.sendButton.innerHTML = '<i class="fas fa-spinner fa-spin"></i>';
        
        // Add typing indicator with glitch effect
        const typingDiv = document.createElement('div');
        typingDiv.className = 'message bot-message typing-indicator';
        typingDiv.id = 'typingIndicator';
        
        const avatar = document.createElement('div');
        avatar.className = 'message-avatar';
        const icon = document.createElement('i');
        icon.className = 'fas fa-brain';
        avatar.appendChild(icon);
        
        const messageContent = document.createElement('div');
        messageContent.className = 'message-content';
        messageContent.innerHTML = '<p>Neural processing...</p>';
        
        typingDiv.appendChild(avatar);
        typingDiv.appendChild(messageContent);
        
        this.chatMessages.appendChild(typingDiv);
        this.scrollToBottom();
        
        // Add glitch effect to typing indicator
        setInterval(() => {
            if (typingDiv.parentNode) {
                this.addGlitchToMessage(typingDiv);
            }
        }, 2000);
    }
    
    hideLoading() {
        this.isLoading = false;
        this.sendButton.disabled = false;
        this.sendButton.innerHTML = '<i class="fas fa-paper-plane"></i>';
        
        // Remove typing indicator
        const typingIndicator = document.getElementById('typingIndicator');
        if (typingIndicator) {
            typingIndicator.remove();
        }
    }
    
    scrollToBottom() {
        this.chatMessages.scrollTop = this.chatMessages.scrollHeight;
    }
}

// Function to ask questions from suggestion chips
function askQuestion(question) {
    // Find the chat input and set the value
    const chatInput = document.getElementById('chatInput');
    chatInput.value = question;
    
    // Trigger the send button
    document.getElementById('sendButton').click();
}

// Add CSS for new animations
const dystopianStyles = document.createElement('style');
dystopianStyles.textContent = `
    @keyframes glitchOut {
        0% { opacity: 1; transform: scale(1); }
        50% { opacity: 0.5; transform: scale(1.1) skew(2deg); }
        100% { opacity: 0; transform: scale(0.9) skew(-2deg); }
    }
    
    @keyframes messageGlitch {
        0%, 100% { transform: translateX(0); }
        25% { transform: translateX(-1px); }
        75% { transform: translateX(1px); }
    }
    
    @keyframes scanLineMove {
        0% { transform: translateY(0); }
        100% { transform: translateY(4px); }
    }
    
    .typing-indicator .message-content p {
        animation: blink 1s infinite;
    }
    
    .message-counter {
        color: #ff00ff !important;
        animation: pulse 2s ease-in-out infinite;
    }
    
    .tv-screen {
        transition: all 0.3s ease;
    }
    
    .tv-screen.glitching {
        filter: hue-rotate(90deg) saturate(2) contrast(1.5);
        transform: skew(0.5deg, 0deg);
    }
`;

document.head.appendChild(dystopianStyles);

// Initialize everything when DOM is loaded
document.addEventListener('DOMContentLoaded', function() {
    // Initialize dystopian chat bot
    const chatBot = new DystopianChatBot();
    
    // Add atmospheric background effects
    addAtmosphericEffects();
    
    // Add TV interaction effects
    addTVEffects();
    
    // Add particle system
    createParticleSystem();
});

function addAtmosphericEffects() {
    // Random atmospheric glitches
    setInterval(() => {
        if (Math.random() < 0.05) {
            document.body.style.filter = 'hue-rotate(180deg)';
            setTimeout(() => {
                document.body.style.filter = 'none';
            }, 100);
        }
    }, 5000);
    
    // Add subtle screen shake on certain events
    document.addEventListener('click', () => {
        if (Math.random() < 0.1) {
            document.body.style.animation = 'screenShake 0.1s ease-in-out';
            setTimeout(() => {
                document.body.style.animation = '';
            }, 100);
        }
    });
}

function addTVEffects() {
    const tvFrame = document.querySelector('.tv-frame');
    
    // Add hover effects
    tvFrame.addEventListener('mouseenter', () => {
        tvFrame.style.transform = 'rotateX(0deg) scale(1.02)';
        tvFrame.style.boxShadow = '0 0 80px rgba(0, 255, 65, 0.5), inset 0 0 50px rgba(0, 0, 0, 0.8)';
    });
    
    tvFrame.addEventListener('mouseleave', () => {
        tvFrame.style.transform = 'rotateX(5deg) scale(1)';
        tvFrame.style.boxShadow = '0 0 50px rgba(0, 255, 65, 0.3), inset 0 0 50px rgba(0, 0, 0, 0.8)';
    });
    
    // Add click effects
    tvFrame.addEventListener('click', () => {
        tvFrame.style.animation = 'tvClick 0.2s ease-in-out';
        setTimeout(() => {
            tvFrame.style.animation = '';
        }, 200);
    });
}

function createParticleSystem() {
    const particleContainer = document.createElement('div');
    particleContainer.className = 'particle-container';
    particleContainer.style.cssText = `
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        pointer-events: none;
        z-index: 1;
    `;
    
    document.body.appendChild(particleContainer);
    
    // Create floating particles
    for (let i = 0; i < 20; i++) {
        createParticle(particleContainer);
    }
}

function createParticle(container) {
    const particle = document.createElement('div');
    particle.style.cssText = `
        position: absolute;
        width: 2px;
        height: 2px;
        background: #00ff41;
        border-radius: 50%;
        opacity: 0.6;
        animation: floatParticle ${5 + Math.random() * 10}s linear infinite;
    `;
    
    particle.style.left = Math.random() * 100 + '%';
    particle.style.top = Math.random() * 100 + '%';
    particle.style.animationDelay = Math.random() * 5 + 's';
    
    container.appendChild(particle);
    
    // Remove and recreate particle when animation ends
    particle.addEventListener('animationend', () => {
        particle.remove();
        createParticle(container);
    });
}

// Add additional CSS for new effects
const additionalStyles = document.createElement('style');
additionalStyles.textContent = `
    @keyframes screenShake {
        0%, 100% { transform: translateX(0); }
        25% { transform: translateX(-1px); }
        75% { transform: translateX(1px); }
    }
    
    @keyframes tvClick {
        0%, 100% { transform: rotateX(5deg) scale(1); }
        50% { transform: rotateX(5deg) scale(0.98); }
    }
    
    @keyframes floatParticle {
        0% { 
            transform: translateY(0) translateX(0);
            opacity: 0.6;
        }
        50% { 
            opacity: 1;
        }
        100% { 
            transform: translateY(-100vh) translateX(${Math.random() * 100 - 50}px);
            opacity: 0;
        }
    }
    
    .particle-container {
        overflow: hidden;
    }
`;

document.head.appendChild(additionalStyles);
