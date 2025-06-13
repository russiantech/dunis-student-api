from django.shortcuts import render

def api_home(request):
    context = {
        "api_base_url": "https://api.dunistech.ng/api/",
        "endpoints": [
            {
                "name": "Courses",
                "list": "/api/courses/",
                "detail": "/api/courses/<id>/",
                "methods": ["GET", "POST", "PUT", "DELETE"]
            },
            {
                "name": "Recipes",
                "list": "/api/recipes/",
                "detail": "/api/recipes/<id>/",
                "methods": ["GET", "POST", "PUT", "DELETE"]
            },
        ],
        "sample_request": {
            "GET": "fetch('https://api.dunistech.ng/api/courses/').then(res => res.json()).then(data => console.log(data));",
            "POST": """axios.post('https://api.dunistech.ng/api/courses/', {
    title: 'New Course',
    description: 'Intro to React'
})"""
        },
        "sample_response": {
            "courses": [{"id": 1, "title": "Flask Basics", "description": "Intro to Flask"}],
            "recipes": [{"id": 1, "title": "Jollof Rice", "ingredients": "Rice, Tomato, Pepper"}]
        }
    }
    return render(request, "landing.html", context)
