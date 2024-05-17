# BAH_Mapper

BAH_Mapper is a web application that visualizes military Basic Allowance for Housing (BAH) rates on an interactive map. This application allows users to select different military pay grades and dependency statuses to dynamically generate and display maps with the corresponding BAH rates for various locations.

## Features

- **Interactive Map**: Visualize BAH rates on a map using Folium and Leaflet.js.
- **Dynamic Data**: Select different pay grades and dependency statuses to update the map in real-time.
- **Geocoding**: Convert city names to latitude and longitude coordinates using the Nominatim geocoding service.
- **Production Ready**: Deployed using Docker, Gunicorn, and Nginx for a robust, scalable, and secure setup.

## Technologies Used

- **Flask**: A lightweight WSGI web application framework in Python.
- **Folium**: A Python wrapper for Leaflet.js maps.
- **Nominatim**: A geocoding service to convert city names to coordinates.
- **Gunicorn**: A Python WSGI HTTP server for UNIX.
- **Nginx**: A high-performance HTTP server and reverse proxy.
- **Docker**: Containerization platform for easy deployment and scalability.
- **Docker Compose**: Tool for defining and running multi-container Docker applications.

## Project Structure

```
BAH_Mapper/
│
├── app.py
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── nginx.conf
├── wsgi.py
├── templates/
│ ├── index.html
├── static/
│ └── data/
│ ├── 2024 BAH Rates.xlsx
│ ├── geocoded_data_With.csv
│ ├── geocoded_data_Without.csv
│ ├── bah_interactive_map_With_E01.html
│ ├── bah_interactive_map_With_E02.html
│ └── (other HTML map files)
```


## Getting Started

### Prerequisites

- Docker
- Docker Compose

### Installation

1. **Clone the repository**:

    ```bash
    git clone https://github.com/your_username/BAH_Mapper.git
    cd BAH_Mapper
    ```

2. **Build and run the Docker containers**:

    ```bash
    docker-compose build
    docker-compose up
    ```

3. **Access the application**:

    Open your web browser and go to `http://127.0.0.1:80/`.

## Usage

- **Select the pay grade and dependency status** from the dropdown menus.
- **Click the "Update Map" button** to generate the corresponding BAH map.

## Configuration

### Dockerfile

Defines the environment and builds the Docker image for the Flask application using Gunicorn.

### docker-compose.yml

Manages the multi-container Docker application, including both the Flask application and Nginx.

### nginx.conf

Configures Nginx to proxy requests to the Flask application.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the GPL-3.0 License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Folium for providing an easy-to-use interface for Leaflet.js.
- Flask for the lightweight web framework.
- Docker for containerization support.
- Nginx and Gunicorn for production-grade web serving capabilities.
