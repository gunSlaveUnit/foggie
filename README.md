# foggie

This project is actually an attempt to copy Steam.

![Store page](desktop/screenshots/screenshot_0.png)

## Used
- PySide6 with QML for desktop application 
- FastAPI as a web server
- Jinja2 to from the admin panel
- PostgreSQL for main data, Redis for user sessions

## Achieved
- Authentication, simple authorization
- It is possible to publish and manage the game (product). For example, change the name, set the price, upload assets, etc.
- Balance replenishment (without a payment system, just adding a number to the database)
- "Purchasing" the game
- Ability to download a purchased game from the library

## Screenshots
![Page 1](desktop/screenshots/screenshot_1.png)

![Page 2](desktop/screenshots/screenshot_2.png)

![Page 3](desktop/screenshots/screenshot_3.png)

![Page 4](desktop/screenshots/screenshot_4.png)

![Page 5](desktop/screenshots/screenshot_5.png)

![Page 6](desktop/screenshots/screenshot_6.png)

![Page 7](desktop/screenshots/screenshot_7.png)

![Page 8](desktop/screenshots/screenshot_8.png)

![Page 9](desktop/screenshots/screenshot_9.png)

![Page 10](desktop/screenshots/screenshot_10.png)

## I would like to do
- Friends and their search, other social functions
- Chat
- Overlay
- Notes
- Sell out, discounts
- Streams
- Game sets
- Game tags and languages settings
- Smart search
- Filters
- Trailers
- Screenshot management
- Cloud
- Dual authentication, login by mail, phone, SMS code
- Recommendation system
- Real time application
- Profile customization
- Present
- Traffic tracking for developers
- Communities
- Marketplace
- Comments, likes, reactions, reposts
- Pause, download speed limit
- DRM
- GDPR
- Some minimal interface
- Emulator of a bunch of consoles? 
- Browser games?

In general, I would like to drop all this and rewrite it normally, without rushing
