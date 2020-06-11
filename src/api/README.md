# How to use the API

Install dev packages: `pipenv install --dev`

Run the following scripts in the API folder (src/api)

To start the API: `uvicorn api:app`

In another terminal run: `python test_api.py`

It will send a post to the API running and print the results.

The code in the `main()` function in `test_api.py` is a reference of how to perform a requests to the API using python requests lib (to be used with streamlit later).

The other way to test the app is just using pytest at the API folder:
`pytest`

There is a warning in this test (numpy.ufunc size changed), I can't figure out how to fix it yet.

# API Documentation

To see API documentation, start the API and access in a browser:

* \<IPADDRESS>:8000/docs - documentation build by swagger
* \<IPADDRESS>:8000/redoc - documentation build using redoc
* \<IPADDRESS>:8000/openapi.json - a JSON file following the (OpenAPI specification)[https://swagger.io/specification/]
