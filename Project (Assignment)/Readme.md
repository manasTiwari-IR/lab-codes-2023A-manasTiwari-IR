
# News Scraper Web Application

## About the Project
The **News Scraper Web Application** is a project designed to scrape and present the latest news headlines along with their associated images. Users can specify a category (e.g., international news, business, innovation etc) to fetch relevant news. The application employs a Python-based backend for web scraping and a modern frontend interface for data presentation.

This project bridges web scraping and interactive web development, allowing users to retrieve dynamic information from a third-party news source ( here bbc.com ) and display it in a visually appealing way.

## Key Features
- Scrapes news headlines, associated images, and additional metadata from a news website (e.g., BBC News).
- Provides the ability to filter news by category.
- Presents the scraped data through an interactive web interface.

## Technologies Used

### Backend
- **Python**: The core language used for web scraping and data processing.
- **Flask**: A lightweight web framework used to create the backend API for the application.
- **BeautifulSoup**: A Python library for parsing HTML and extracting relevant data from web pages.
- **Requests**: A library for making HTTP requests to fetch web page content.

### Frontend
- **HTML**: The structure of the web page.
- **CSS**: For styling the web interface.
- **JavaScript (Axios)**: To interact with the Flask backend and dynamically display news data.

### Additional Tools
- **Flask-CORS**: Enables cross-origin requests, allowing the frontend and backend to communicate seamlessly.

## Workflow
1. **User Input**: The user specifies a news category through the frontend.
2. **Backend Processing**: The Flask backend receives the request and uses the Requests and BeautifulSoup libraries to scrape relevant news from the specified website.
3. **Data Filtering and Saving**: Data is filtered to remove invalid or placeholder images.
4. **Frontend Display**: The data is sent to the frontend and displayed in a clean, user-friendly interface.

## How It Works
### Backend
- **Flask Endpoint**: The `/scrape` endpoint receives a GET request with a query parameter specifying the news category.
- **Web Scraping**: Using BeautifulSoup, the backend extracts headlines, images, and paragraphs from the targeted news website.
- **Response**: The backend responds with a JSON object containing the filtered news data.

### Frontend
- **Axios**: The frontend sends requests to the backend using the Axios and retrieves the scraped data.
- **Dynamic Rendering**: JavaScript dynamically renders the data into the webpage, providing a seamless user experience.

## Challenges and Solutions
### CORS Issues
- **Challenge**: Cross-origin requests between the frontend and backend caused errors.
- **Solution**: Implemented `Flask-CORS` to allow requests from different origins.

### Placeholder Images
- **Challenge**: Some scraped images were placeholders, reducing the quality of the output.
- **Solution**: Filtered out entries with missing or placeholder images.

## Future Improvements
- Add support for scraping from multiple news sources.
- Implement user authentication and personalized news feeds.
- Enhance the web interface with frameworks like React or Angular.
- Use a database to store and retrieve historical news data.

## Conclusion
The News Scraper Web Application demonstrates the power of combining web scraping with web development. It provides users with a practical and interactive tool for staying updated on the latest news in their areas of interest.
