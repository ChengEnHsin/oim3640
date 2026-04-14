## My Project Proposal

**What I'm building:** A Flask web application that helps users find the nearest MBTA transit station by entering an address or place name with time left for the next train to come.

**Why I chose this:** I use public transit way more back home and realized I often find the features can be less developed in the States compared to Taiwan. I hope this app solves the inconvenience by combining real-world APIs (Mapbox for location data and MBTA for transit info) into a practical tool I can actually use. It's also a great way to learn how to build full-stack web applications that interact with external services.

**Core features:**
* Address/place name input field with form validation
* Geocoding integration using Mapbox API to convert addresses to coordinates
* MBTA API query to find the nearest transit station
* Display station details (name, distance, upcoming departures)
* Real-time countdown timer showing minutes until next train arrives
* Live time updates that refresh every second without page reload (using JavaScript)
* Interactive map view showing the address location and nearest station
* Responsive design that works on mobile devices

**What I don't know yet:**
* How to integrate Mapbox and MBTA APIs efficiently and handle rate limiting
* Best practices for storing and managing API keys securely in Flask
* How to calculate distances and sort results from multiple MBTA stops
* Map rendering libraries and how to embed them in a Flask template
* Error handling for invalid addresses or locations outside MBTA coverage area
* How to implement live countdown timers with JavaScript that update in real-time
* How to handle timezone differences and ensure accurate departure time calculations
* Best approach for syncing client-side timers with server data without constant API calls