# Mozio Coding Task

## Prompt:

As Mozio expands internationally, we have a growing problem that many transportation suppliers we'd like to integrate cannot give us concrete zip codes, cities, etc that they serve.

To combat this, we'd like to be able to define custom polygons as their "service area" and we'd like for the owners of these shuttle companies to be able to define and alter their polygons whenever they want, eliminating the need for mozio employees to do this boring grunt work.

## Requirement:

Build a JSON REST API with CRUD operations for Provider (name, email, phone number, language an currency) and ServiceArea (name, price, geojson information)

Create a specific endpoint that takes a lat/lng pair as arguments and return a list of all polygons that include the given lat/lng. The name of the polygon, provider's name, and price should be returned for each polygon. This operation should be FAST.

Use unit tests to test your API;

Write up some API docs (using any tool you see fit);

Create a Github account (if you don’t have one), push all your code and share the link with us;

Deploy your code to a hosting service of your choice. Mozio is built entirely on AWS, so bonus
