Skilled Front-End Vue.js Developer Needed for Web Application


We are developing a web application called "Ville de rêve Pro" ("Dream City"). The app gives users access to a wide range of data about French cities — covering population, housing, employment, health, and more.
We are looking for a Vue.js front-end developer to help us build the user interface of the app.

🧩 Application Structure
The app is divided into three parts:
- Static pages – homepage, terms & conditions, press room, etc.
- Transactional section – cart, payment confirmation, user login, client dashboard, etc.
- Main app / city dashboard – each city has a dedicated page with detailed data.

🛠️ Objective
To develop the front-end (desktop and responsive mobile), integrating Figma designs and connecting it to our existing REST API (currently being finalized)



🎨 Design
Figma designs will be provided. You can have a look here:

https://www.figma.com/design/PH4eGlQVyjo57QJ1WUrcJh/ville-de-reve?node-id=0-1&t=PIAiJuN0MomRxkg7-1




Tech Stack
- Vite
- Vue.js with Composition API
- Tailwind CSS
- Pinia
- Axios
- E-charts
- WebDataRocks
- Leaflet
The front-end consumes a REST API currently under development.

🎯 Project Phases
- Build all pages in static mode (based on Figma)
- Connect the front-end to the API once finalized

📅 Timeline & Budget
- Start: ASAP
- Duration: 3–4 weeks
- Communication: English, via Upwork + GitHub
- Milestones:
-- Homepage
-- City Dashboard Page
-- Secondary Pages
-- API Integration
- Budget: $800




Full brief with detailed behavior of each pages is available here:

🌐 Project Brief – Front-End Vue.js Developer for “Ville de rêve” Web App
📘 Project Overview
We are developing a web application called "Ville de rêve Pro" ("Dream City"). The app gives users access to a wide range of data about French cities — covering population, housing, employment, health, and more.
We are looking for a Vue.js front-end developer to help us build the user interface of the app.

🧩 Application Structure
The app is divided into three parts:
Static pages – homepage, terms & conditions, press room, etc.


Transactional section – cart, payment confirmation, user login, client dashboard, etc.


Main app / city dashboard – each city has a dedicated page with detailed data.



🛠️ Objective
To develop the front-end (desktop and responsive mobile), integrating Figma designs and connecting it to our existing REST API (currently being finalized).

🎨 Design
Figma designs are provided:
https://www.figma.com/design/PH4eGlQVyjo57QJ1WUrcJh/ville-de-reve?node-id=0-1&t=DreFIHmJ98brTi1h-1
Prototype: https://www.figma.com/proto/PH4eGlQVyjo57QJ1WUrcJh/ville-de-reve?node-id=104-804&p=f&t=hEZuGXdJqyySBj4F-1&scaling=min-zoom&content-scaling=fixed&page-id=0%3A1&starting-point-node-id=104%3A804&show-proto-sidebar=1


💻 Tech Stack
Vite
Vue.js with Composition API
Tailwind CSS
Pinia
Axios
Echarts
WebDataRocks
Leaflet
The front-end consumes a REST API currently under development.



🚦Technical Notes
❗ No external libraries or components may be added without approval — performance and load speed are critical.


❗ The homepage, static pages, and city dashboard page must be separate routes/components with lazy loading. The homepage must not preload dashboard components.



🧭 Homepage Behavior
Mostly static content.
A city search input allows users to search for cities.
"Key Indicators" is a carousel of thematic tiles. Clicking a category scrolls directly to the related slide.
When the user types at least 3 characters, call the API to suggest matching cities (autocomplete behavior).
Clicking on a city result (or if only one result is available) redirects to that city’s page.
Clicking "Access the data" without a selected city should trigger an error popup.
Footer:  newsletter subscription is dealt with SendInBlue

📊 City Dashboard Behavior
Header
Category selector: Clicking opens a dropdown list of data themes.
Search field: Autocomplete powered by the API. Clicking a result scrolls to the relevant data block.
Settings:
Opens a right panel when the gear icon is clicked.


Main section width is adjustable (default: 1/2) on desktop.
User can select a comparison year.
User can compare with selected organizations or regions.
Option to show/hide data forecasts.
Copy/shareable link for the current view (with the access token).
Sticky header (desktop & mobile).



👥 User Access Behavior
If the user is not logged in / doesn't have a valid access token:
The city dashboard is shown in demo mode, with dummy data and "demo" notices at the top and bottom.
Multiple "Add to cart" or "Enter your token" call-to-action blocks appear.


If the user has a valid token:
Real data is shown, and demo blocks are hidden.
Data is sent by the API.



🏙️ Main City View
Displays general city information fetched via the API.
"Explore by category" updates the dashboard with the selected data theme.



📚 Thematic City View
Each theme (housing, health, etc.) is accessible via a clean URL
 (e.g. app.villedereve.fr/74010-annecy-34Jtjzo64er36jr/housing)


The API provides:
List of data blocks per theme
Each block has a title, optional subtitle, analysis text, forecast text, and a list of data points.
Each data point includes title, subtitle, value, unit, text (optional), and time evolution.


Evolution blocks (trend icons/colors) are generated in JavaScript from the data.
Each block includes one or more charts:
Line, bar, pie, radar, scatter plots (echarts), and maps (Leaflet).
Sticky content behavior for left/right blocks depending on height (only on desktop).
Charts rendered using Echarts.
A pivot table (bottom of page) powered by WebDataRocks (with custom theme).
Maps powered by Leaflet, with helper functions provided.



⚙️ JavaScript Logic for City Dashboard
API calls must include:
User token
Unique city ID
If the user doesn’t have the right authorization / a wrong token, an error message is displayed and demo data is sent.
Functions to build the page must support:
The selected reference year for chart and text
Comparison subjects for chart and text
Forecasts toggle on chart


Settings must be stored in Pinia store



💳 Transactional Pages
Access Token Page
Full access to a city dashboard requires a token.
Users can input it manually or request it via email on a "Forgot Token" page.
Cart & Payment Flow
Users can add cities to their cart from the dashboard.
Payments are processed via Stripe.
After payment, users are redirected to a "Thank You" page listing accessible cities.
The token is stored in Pinia for further API usage.



🎯 Project Phases
Build all pages in static mode (based on Figma)
Connect the front-end to the API once finalized



📅 Timeline & Budget
Start: ASAP
Duration: 3–4 weeks
Communication: English, via Upwork + GitHub
Milestones:
Homepage
City Dashboard Page
Secondary Pages
API Integration
Budget: $800

Thank you for your attention,

Jérôme





Skills and Expertise
Front-End Development Skills
Tailwind CSS
Front-End Development Deliverables
Web Application
Other
Vue.js
JavaScript
CSS
HTML
HTML5