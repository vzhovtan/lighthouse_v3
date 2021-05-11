### Lighthouse V3

Lighthouse is developed by Cisco TAC engineers for engineers providing common resource of useful commands and support links to help in troubleshooting.


Lighthouse is internal project and has been created with idea to use BDB as a backend and JS as frontend on CSOne. V1 and V2 were created purely with JS and all information has been saved in .txt files.

BDB aka Big Data Broker is internal Cisco backend to run custom Python and JS scripts and using MongoDB as database. Current version of Lighthouse utilizes MongoDB and saves data in different collections for different platforms. Each entry in DB represents particular feature as a key and contains troubleshooting information as value.

BDB supports REST API and so Lighthouse backend built with Python using REST API to BDB for ingesting data into MongoDB or retrieving the data from database.

There are two frontends are created with JS. Admin one includes functions to update DB, get usage statistics and so on.
This one built with:

* `bdb_add_update_final.html`
* `bdb_admin_final.html`
* `bdb_get_stats_final.html`
* `bdb_guide_final.html`
* `bdb_index_final.html`
* `bdb_user_view_final.html`

Second frontend designed to run in Salesforce CSOne app using Greasemonkey and Tampermonkey:

* `lighthouse_v3_frontend_final.js`

Backend file is:

* `lighthouse_v3_backend.py`

There are couple additional backends files created to collect statistics of Lighthouse usage and save it in MongoDB:

* `lighthouse_v3_statistics_v1.0.py`
* `ighthouse_v3_statistics_v2.0.py`
