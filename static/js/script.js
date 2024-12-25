// Time-based welcome message function
function getTimeBasedMessage(messages) {
    const hour = new Date().getHours();
    
    if (hour >= 5 && hour < 12) {
        return messages.morning;
    } else if (hour >= 12 && hour < 17) {
        return messages.afternoon;
    } else if (hour >= 17 && hour < 21) {
        return messages.evening;
    } else {
        return messages.night;
    }
}

async function loadContent() {
    try {
        console.log('Fetching links data...');
        const response = await fetch('/api/links');
        console.log('Response received:', response);
        
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        
        const data = await response.json();
        console.log('Data received:', data);

        if (!data || !data.links) {
            console.error('Invalid data format received:', data);
            return;
        }

        const linksContainer = document.getElementById('links-container');
        if (!linksContainer) {
            console.error('Links container not found');
            return;
        }

        // Sort links by category
        const categories = {};
        data.links.forEach(link => {
            if (!categories[link.category]) {
                categories[link.category] = [];
            }
            categories[link.category].push(link);
        });

        // Create category sections
        Object.keys(categories).forEach(category => {
            const categorySection = document.createElement('div');
            categorySection.className = 'category-section';

            const categoryTitle = document.createElement('h2');
            categoryTitle.textContent = category;
            categorySection.appendChild(categoryTitle);

            const linksGrid = document.createElement('div');
            linksGrid.className = 'links-grid';

            categories[category].forEach(link => {
                const linkCard = document.createElement('a');
                linkCard.href = link.url;
                linkCard.className = 'link-card';
                linkCard.target = link.url.startsWith('http') ? '_blank' : '_self';

                // Check if the icon is an MDI icon or an image URL
                const iconContent = link.icon.startsWith('mdi') 
                    ? `<i class="${link.icon}"></i>`
                    : `<img src="${link.icon}" alt="${link.name}">`;

                linkCard.innerHTML = `
                    <div class="link-icon">
                        ${iconContent}
                    </div>
                    <div class="link-info">
                        <h3>${link.name}</h3>
                        <p>${link.description || ''}</p>
                    </div>
                `;

                linksGrid.appendChild(linkCard);
            });

            categorySection.appendChild(linksGrid);
            linksContainer.appendChild(categorySection);
        });

    } catch (error) {
        console.error('Error loading content:', error);
        const linksContainer = document.getElementById('links-container');
        if (linksContainer) {
            linksContainer.innerHTML = '<p>Error loading content. Please try again later.</p>';
        }
    }
}

// Call loadContent when the page loads
document.addEventListener('DOMContentLoaded', () => {
    console.log('DOM Content Loaded, calling loadContent');
    loadContent();
}); 