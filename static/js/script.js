// Divine light orb interface for Alex Gu
class DivineInterface {
    constructor() {
        this.messageDisplay = document.getElementById('messageDisplay');
        this.messageInput = document.getElementById('messageInput');
        this.sendButton = document.getElementById('sendButton');
        this.messageInterface = document.getElementById('messageInterface');
        this.divineName = document.getElementById('divineName');
        this.divinePresence = document.getElementById('divinePresence');
        this.isLoading = false;
        this.messageCount = 0;
        
        this.initializeEventListeners();
        this.initializeDivineInterface();
    }
    
    initializeEventListeners() {
        // Send message on button click
        this.sendButton.addEventListener('click', () => this.sendMessage());
        
        // Send message on Enter key
        this.messageInput.addEventListener('keypress', (e) => {
            if (e.key === 'Enter' && !e.shiftKey) {
                e.preventDefault();
                this.sendMessage();
            }
        });
        
        // Auto-resize input
        this.messageInput.addEventListener('input', () => {
            this.messageInput.style.height = 'auto';
            this.messageInput.style.height = this.messageInput.scrollHeight + 'px';
        });
    }
    
    initializeDivineInterface() {
        // Add divine name animations
        this.addDivineNameAnimations();
        
        // Add orb interactions
        this.addOrbInteractions();
        
        // Add divine presence effects
        this.addDivinePresenceEffects();
        
        // Zen experience: immediate long fade-in over 5 seconds
        this.startDivineInteraction();
    }
    
    addDivineNameAnimations() {
        // Add subtle hover effect to name
        this.divineName.addEventListener('mouseenter', () => {
            this.divineName.style.transform = 'scale(1.02)';
            this.divineName.style.transition = 'transform 0.4s cubic-bezier(0.25, 0.46, 0.45, 0.94)';
        });
        
        this.divineName.addEventListener('mouseleave', () => {
            this.divineName.style.transform = 'scale(1)';
        });
    }
    
    addOrbInteractions() {
        // Add orb response to typing
        this.messageInput.addEventListener('input', () => {
            if (this.messageInput.value.length > 0) {
                this.activateOrb();
            } else {
                this.deactivateOrb();
            }
        });
        
        // Add orb response to focus
        this.messageInput.addEventListener('focus', () => {
            this.activateOrb();
        });
        
        this.messageInput.addEventListener('blur', () => {
            if (this.messageInput.value.length === 0) {
                this.deactivateOrb();
            }
        });
    }
    
    addDivinePresenceEffects() {
        // Add very subtle presence animations for zen experience
        setInterval(() => {
            if (Math.random() < 0.05) {
                this.divinePresence.style.opacity = '0.8';
                setTimeout(() => {
                    this.divinePresence.style.opacity = '0.7';
                }, 400);
            }
        }, 12000);
        
        // Add minimal orb particle effects
        const orbParticles = document.querySelector('.orb-particles');
        if (orbParticles) {
            setInterval(() => {
                if (Math.random() < 0.08) {
                    orbParticles.style.opacity = '0.5';
                    setTimeout(() => {
                        orbParticles.style.opacity = '0.4';
                    }, 500);
                }
            }, 10000);
        }
    }
    
    activateOrb() {
        // Make orb more active when user is typing
        const orbCore = document.querySelector('.orb-core');
        const orbGlow = document.querySelector('.orb-glow');
        
        if (orbCore && orbGlow) {
            orbCore.style.filter = 'blur(30px)';
            orbGlow.style.opacity = '0.9';
            orbGlow.style.transform = 'translate(-50%, -50%) scale(1.2)';
        }
    }
    
    deactivateOrb() {
        // Return orb to normal state
        const orbCore = document.querySelector('.orb-core');
        const orbGlow = document.querySelector('.orb-glow');
        
        if (orbCore && orbGlow) {
            orbCore.style.filter = 'blur(40px)';
            orbGlow.style.opacity = '0.6';
            orbGlow.style.transform = 'translate(-50%, -50%) scale(1)';
        }
    }
    
    startDivineInteraction() {
        // Start the long 5-second fade-in immediately
        this.messageInterface.style.transition = 'all 5s cubic-bezier(0.25, 0.46, 0.45, 0.94)';
        this.messageInterface.style.opacity = '0';
        this.messageInterface.style.transform = 'translateY(20px) scale(0.98)';
        
        // Gradually fade in the message interface
        setTimeout(() => {
            this.messageInterface.style.opacity = '1';
            this.messageInterface.style.transform = 'translateY(0) scale(1)';
        }, 100);
        
        // Fade out divine presence slowly
        this.divinePresence.style.transition = 'all 3s cubic-bezier(0.25, 0.46, 0.45, 0.94)';
        this.divinePresence.style.opacity = '0';
        
        // Add divine welcome message after fade-in completes
        setTimeout(() => {
            this.addDivineMessage("I am listening. What would you like to know about my background, projects, and experience?", 'bot');
            
            // Focus on input
            this.messageInput.focus();
            
            // Activate orb
            this.activateOrb();
        }, 5000);
    }
    
    async sendMessage() {
        const message = this.messageInput.value.trim();
        if (!message || this.isLoading) return;
        
        // Add user message
        this.addDivineMessage(message, 'user');
        this.messageInput.value = '';
        this.messageInput.style.height = 'auto';
        
        // Show divine loading
        this.showDivineLoading();
        
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
                this.addDivineMessage(data.response, 'bot');
                
                // Add divine response effects
                this.addDivineResponseEffects();
            } else {
                // Show divine error message
                this.addDivineMessage("I am having a moment. Could you try asking that again?", 'bot');
            }
        } catch (error) {
            console.error('Error:', error);
            this.addDivineMessage("Something is interfering with our connection. Let me try to reconnect...", 'bot');
        } finally {
            this.hideDivineLoading();
        }
    }
    
    addDivineResponseEffects() {
        // Add divine name aura effect
        const nameAura = document.querySelector('.name-aura');
        if (nameAura) {
            nameAura.style.opacity = '0.8';
            nameAura.style.transform = 'translate(-50%, -50%) scale(1.3)';
            
            setTimeout(() => {
                nameAura.style.opacity = '0.4';
                nameAura.style.transform = 'translate(-50%, -50%) scale(1)';
            }, 1000);
        }
        
        // Add orb pulse effect
        const orbCore = document.querySelector('.orb-core');
        if (orbCore) {
            orbCore.style.transform = 'translate(-50%, -50%) scale(1.1) rotate(2deg)';
            
            setTimeout(() => {
                orbCore.style.transform = 'translate(-50%, -50%) scale(1) rotate(0deg)';
            }, 500);
        }
        
        // Add ethereal mist effect
        const etherealMist = document.querySelector('.ethereal-mist');
        if (etherealMist) {
            etherealMist.style.opacity = '0.6';
            etherealMist.style.transform = 'scale(1.2)';
            
            setTimeout(() => {
                etherealMist.style.opacity = '0.3';
                etherealMist.style.transform = 'scale(1)';
            }, 800);
        }
        
        // Add glossy bubble effects
        this.addGlossyBubbleEffects();
        
        // Add interface glow effect
        this.messageInterface.style.boxShadow = '0 35px 100px rgba(255, 255, 255, 0.5)';
        
        setTimeout(() => {
            this.messageInterface.style.boxShadow = '0 25px 80px rgba(255, 255, 255, 0.3)';
        }, 1200);
    }
    
    addGlossyBubbleEffects() {
        // Add glossy highlight sweep to message interface
        const messageInterface = this.messageInterface;
        messageInterface.style.animation = 'none';
        messageInterface.offsetHeight; // Trigger reflow
        
        // Create glossy sweep effect
        const glossySweep = document.createElement('div');
        glossySweep.style.cssText = `
            position: absolute;
            top: 0;
            left: -100%;
            width: 100%;
            height: 100%;
            background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.6), transparent);
            transition: left 1s ease;
            pointer-events: none;
            z-index: 1;
            border-radius: 30px;
        `;
        
        // Don't change the position - keep it absolute for proper centering
        messageInterface.appendChild(glossySweep);
        
        // Trigger the sweep
        setTimeout(() => {
            glossySweep.style.left = '100%';
        }, 100);
        
        // Remove the element after animation
        setTimeout(() => {
            if (glossySweep.parentNode) {
                glossySweep.remove();
            }
        }, 1100);
        
        // Add bubble bounce effect
        messageInterface.style.transform = 'scale(1.05) translateY(-5px)';
        messageInterface.style.transition = 'transform 0.6s cubic-bezier(0.25, 0.46, 0.45, 0.94)';
        
        setTimeout(() => {
            messageInterface.style.transform = 'scale(1) translateY(0)';
        }, 600);
    }
    
    addDivineMessage(content, sender) {
        this.messageCount++;
        
        const messageDiv = document.createElement('div');
        messageDiv.className = `message ${sender}-message`;
        
        const paragraph = document.createElement('p');
        paragraph.textContent = content;
        messageDiv.appendChild(paragraph);
        
        this.messageDisplay.appendChild(messageDiv);
        
        // Scroll to bottom
        this.scrollToBottom();
        
        // Add divine entrance animation
        setTimeout(() => {
            messageDiv.style.animation = 'messageSlideIn 0.8s ease-out';
        }, 100);
        
        // Add divine hover effect
        messageDiv.addEventListener('mouseenter', () => {
            messageDiv.style.transform = 'translateX(8px)';
            messageDiv.style.transition = 'transform 0.4s cubic-bezier(0.25, 0.46, 0.45, 0.94)';
        });
        
        messageDiv.addEventListener('mouseleave', () => {
            messageDiv.style.transform = 'translateX(0)';
        });
    }
    
    showDivineLoading() {
        this.isLoading = true;
        this.sendButton.disabled = true;
        this.sendButton.innerHTML = '<i class="fas fa-spinner fa-spin"></i>';
        
        // Add divine loading indicator
        const loadingDiv = document.createElement('div');
        loadingDiv.className = 'message bot-message loading-message';
        loadingDiv.id = 'loadingMessage';
        
        const loadingIndicator = document.createElement('div');
        loadingIndicator.className = 'loading-indicator';
        loadingIndicator.innerHTML = `
            <span>Listening</span>
            <div class="loading-dots">
                <div class="loading-dot"></div>
                <div class="loading-dot"></div>
                <div class="loading-dot"></div>
            </div>
        `;
        
        loadingDiv.appendChild(loadingIndicator);
        this.messageDisplay.appendChild(loadingDiv);
        this.scrollToBottom();
        
        // Add orb pulse during loading
        this.activateOrb();
    }
    
    hideDivineLoading() {
        this.isLoading = false;
        this.sendButton.disabled = false;
        this.sendButton.innerHTML = '<i class="fas fa-arrow-up"></i>';
        
        // Remove loading message
        const loadingMessage = document.getElementById('loadingMessage');
        if (loadingMessage) {
            loadingMessage.remove();
        }
        
        // Return orb to normal state
        this.deactivateOrb();
    }
    
    scrollToBottom() {
        this.messageDisplay.scrollTop = this.messageDisplay.scrollHeight;
    }
}

// Function to ask questions from divine question lights
function askQuestion(question) {
    // Find the message input and set the value
    const messageInput = document.getElementById('messageInput');
    messageInput.value = question;
    
    // Trigger the send button
    document.getElementById('sendButton').click();
}

// Add CSS for divine animations
const divineStyles = document.createElement('style');
divineStyles.textContent = `
    .divine-name {
        transition: transform 0.4s cubic-bezier(0.25, 0.46, 0.45, 0.94);
    }
    
    .orb-core {
        transition: all 0.6s cubic-bezier(0.25, 0.46, 0.45, 0.94);
    }
    
    .orb-glow {
        transition: all 0.6s cubic-bezier(0.25, 0.46, 0.45, 0.94);
    }
    
    .orb-particles {
        transition: opacity 0.4s ease;
    }
    
    .ethereal-mist {
        transition: all 0.8s ease;
    }
    
    .name-aura {
        transition: all 0.6s cubic-bezier(0.25, 0.46, 0.45, 0.94);
    }
    
    .message {
        transition: transform 0.4s cubic-bezier(0.25, 0.46, 0.45, 0.94);
    }
    
    .divine-input {
        transition: all 0.4s cubic-bezier(0.25, 0.46, 0.45, 0.94);
    }
    
    .divine-send {
        transition: all 0.4s cubic-bezier(0.25, 0.46, 0.45, 0.94);
    }
    
    .question-light {
        transition: all 0.4s cubic-bezier(0.25, 0.46, 0.45, 0.94);
    }
    
    .divine-message-interface {
        transition: all 1s cubic-bezier(0.25, 0.46, 0.45, 0.94);
    }
    
    .divine-presence {
        transition: all 0.6s ease;
    }
`;

document.head.appendChild(divineStyles);

// Initialize everything when DOM is loaded
document.addEventListener('DOMContentLoaded', function() {
    // Initialize divine interface
    const divineInterface = new DivineInterface();
    
    // Add additional divine touches
    addDivineTouches();
});

function addDivineTouches() {
    // Minimal divine cursor interactions for zen experience
    document.addEventListener('mousemove', (e) => {
        if (Math.random() < 0.001) {
            const orbParticles = document.querySelector('.orb-particles');
            if (orbParticles) {
                orbParticles.style.opacity = '0.5';
                setTimeout(() => {
                    orbParticles.style.opacity = '0.4';
                }, 300);
            }
        }
    });
    
    // Remove scroll interactions for zen experience
    
    // Remove resize effects for zen experience
    
    // Add divine presence to typing
    const messageInput = document.getElementById('messageInput');
    if (messageInput) {
        messageInput.addEventListener('input', () => {
            const divinePresence = document.querySelector('.divine-presence');
            if (divinePresence && messageInput.value.length > 0) {
                divinePresence.style.opacity = '0.9';
                setTimeout(() => {
                    divinePresence.style.opacity = '0.7';
                }, 200);
            }
        });
    }
}
