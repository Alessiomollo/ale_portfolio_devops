# ale_portfolio_devops

With this app you are able to CRUD users.

Table:
    Users
        id SERIAL
        first_name TEXT NON NULL,
        last_name TEXT NON NULL,
        email EMAIL NON NULL UNIQUE

endpoints:
    Users


API:
    127.0.0.1:800 = home page
    ''/users/ = CRUD
    ''/users/# = GET id