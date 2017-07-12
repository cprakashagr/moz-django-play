# **Django Rest Framework**

First application for Django and Rest Framework with MongoDB. To enable faster retrieval, `redis` has been used.

A provider is an identity which provides services around a geo-fenced polygon. The userEndPoint is an API which can find the intersection and return the list of providers who can service.

### **Usage**

run `django`:
```bash
python manage.py runserver 8000
OR
gunicorn --access-logfile - --workers 4 --bind=0.0.0.0:8000 Mozio.wsgi:application
```

providers:
```bash
GET, POST, PUT, PATCH, DELETE `http://localhost:8000/api/providers/`
```

polygons:
```bash
GET, POST, PUT, PATCH, DELETE at http://localhost:8000/api/polygons/
```

To access endpoints:
```
GET at http://localhost:8000/api/userEndPoint?lnlt=0.5,0.5
```
application/json Raw data for Provider:
```json
{
    "id": "5963ecde8be4ca1877dbdaec",
    "name": "Hello Me14567",
    "email": "HelloMe@1.com",
    "phoneNumber": "+911234567890",
    "language": "en",
    "currency": "INR"
}
```

application/json Raw data for Polygons:
```json
{
        "id": "59661257bbe536d309fac03c",
        "name": "bellandur",
        "price": 52,
        "geometry": {
            "type": "Polygon",
            "coordinates": [
                [
                    [
                        0,
                        0
                    ],
                    [
                        2,
                        0
                    ],
                    [
                        2,
                        2
                    ],
                    [
                        0,
                        2
                    ],
                    [
                        0,
                        0
                    ]
                ]
            ]
        },
        "providerId": "596635558be4ca35daec9243"
    }
```

##### **TODO**

1. For a new polygon entry, modify redis cache
2. Documentation
