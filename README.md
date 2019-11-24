# drf

## Startup of the service:

Assuming you have python and pipenv already setup in your box.
Run these commands:
```
git clone https://github.com/shouro/drf.git
cd drf
pipenv --python 3.6
pipenv shell
pipenv install
pytohn manage.py runserver
```
**Test the API:**
```
localhost:8000/admin
http://localhost:8000/apis/v1/
```
**Docker:**
```
docker-compose build
docker-compose up
```
## Use Cases:

GET /apis/v1/products/
Returns a list of all product:
```
[
    {
        "id": 6,
        "name": "Hulk Mug",
        "slug": "hulk-mug",
        "code": "2367"
    },
    {
        "id": 5,
        "name": "Small hulk",
        "slug": "small-hulk",
        "code": "3490"
    },
    {
        "id": 4,
        "name": "Mario Mug",
        "slug": "mario-mug",
        "code": "1998"
    }
]
```

POST /apis/v1/products/
Input a dict or list of dict
```
{
    "name": "Spider Mug",
    "slug": "spider-mug",
    "code": "3670"
}
```

OR

```
[
    {
        "name": "Spider Mug",
        "slug": "spider-mug",
        "code": "3670"
    },
    {
        "name": "khatta",
        "slug": "khatta-mu",
        "code": "4901"
    }
]
```
Returns a newly created entry or list

GET apis/v1/products/<id>/
Detail of an entry

PUT apis/v1/products/<id>/
Update an entry
Input:
```
{
    "id": <ID>,
    "name": "Wario Mug",
    "slug": "Wario-mug",
    "code": "1998"
}
```

DELETE apis/v1/products/<id>/
Delete an entry

GET apis/v1/products/<id>/attributes/
Returns products attribuates list

POST apis/v1/products/<id>/attributes/
create products new attribuate
```
{
    "property": "color",
    "value": "red"
}
```

PUT apis/v1/products/<id>/attributes/
update a attribute
```
{
    "id": 7,
    "property": "color",
    "value": "pink"
}
```
DELETE apis/v1/products/<id>/attributes/?id=attr_id
delete attribute by attr_id

GET apis/v1/products/<id>/prices/
Returns products price list

POST apis/v1/products/<id>/prices/
create products new price
```
{
    "property": "150",
    "begin_date": "yyyy-mm-dd"
    "end_date": "yyyy-mm-dd"
}
```
PUT apis/v1/products/<id>/prices/
update a price and its date range
```
{
    "id": 7,
    "property": "200",
    "begin_date": "yyyy-mm-dd"
    "end_date": "yyyy-mm-dd"
}
```
DELETE apis/v1/products/<id>/prices/?id=price_id
delete attribute by price_id