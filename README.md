# TripSphere — Project 11
Local educational hotel reservation prototype. Next.js, Express, PostgreSQL and FastAPI.

## Run
Install Docker Desktop. Copy `.env.example` to `.env` and replace JWT_SECRET with a random 32+ character value. Run `docker compose up --build`. Open http://localhost:3000; API health http://localhost:4000/health; pricing Swagger http://localhost:8000/docs.

## Architecture
Browser → Express → PostgreSQL. Separate FastAPI quote service (not connected to checkout). Room row locks serialize hold creation; overlapping half-open date intervals conflict. Expired holds are ignored after cleanup on the next hold request. Payment simulation updates the booking under a row lock. Prices are integer paise in booking records. Demo identity is anonymous, stored in browser local storage; not production authentication.

## API
GET /rooms?city=; POST /demo-login; POST /holds (room_id, arrival, departure); GET /bookings; POST /bookings/:id/pay (simulate_failure optional); POST /bookings/:id/cancel. Booking endpoints require Bearer token. Cancellation releases inventory but does not implement refunds.

## Tests
`node --check api/index.js`; `cd pricing && pip install -r requirements.txt && pytest`. Docker and concurrency integration tests still required.

## Assessment status
1 partial UI; 2 partial booking APIs; 3 partial schema; 4 demo ownership only; 5 partial standalone pricing; 6 search only, no recommendation service; 7 partial consistency engine, no scheduled expiry; 8 simulated payment only; 9 partial Docker stack, no Redis/worker; 10 Git collaboration not performed; 11 basic CI configuration, no deployment; 12 incomplete tests; 13 basic API documentation; 14 not deployed; 15 incident exercises not performed. No real payment, refund, manager portal, email or external integrations. Use synthetic data only. Do not expose publicly.
