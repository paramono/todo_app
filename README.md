# Todo test project for data-cubed.co.uk

Task: build a simple todo list web app using Django and Nuxt, it should support the following:

- Adding new items
- Listing existing items
- Marking items as completed

Notes for implementation:

- The Django backend must store list items in a model
- The Vue.js / Nuxt frontend must only communicate with the backend using an API such as REST or GraphQL
- The code should be pushed to GitHub for review

## Installation

```
docker-compose -f local.yml build
docker-compose -f local.yml up
```

Note: to create this project, I used my own automated django project template which helps me avoid writing configuration boilerplate from scratch.

That being said, you will notice multiple docker compose files (local.yml and production.yml). For this test, I have been working only on local deployment scenario, to demonstrate how I'd usually start working on a project using my development machine. While I didn't add anything of importance to production files here, I am still leaving them to show how I can hypothetically handle different deployment scenarios.


## Project layout

- Backend code in the root directory
- Frontend code in todo_front subdirectory

In real world, backend and frontend might be stored in separate git repositories, but I kept everything in the same repo for the sake of simplicity.

## Backend notes

- Django Rest Framework is used for REST API
- I haven't implemented auth/Users yet, but hopefully I will have enough time to finish that. In the meantime, all REST API endpoints have AllowAny permissions configured to make this app usable without auth.
- I decided that handling item reordering is an overkill for this project, hence by default all models are ordered by id
- Pagination is implemented for lists (ListContainer model). Number of lists per page is set to 3, so that it doesn't take too much typing before you can see pagination in action.
- Lists and items have separate endpoints in this project, but this could have been implemented in a few different ways:
  - Endpoint for items could have been nested within lists endpoint, i.e.: 'lists/{id}/items'
  - Items could have been handled as a field of lists, without a separate items endpoint. However, this would makes List serializer more complex for item creation, patching and removing
- List serializer (ListContainerSerializer) returns all its items through a nested ListItemSerializer

## Frontend notes

- pug is used to make markup more readable
- bootstrap-vue is used, since it's relevant to the stack used by your company
- UI/UX is fairly basic, just showing how I would handle nuxt/vue
- List/item name is updated on input with debouncing
