# Tables

## Data Tables

### USER

#### All Required
| Field             | Description                   |
| ----------------- |:------------------------------|
| username          | unique char(128)              |
| email             | unique char(128)              |
| first\_name       | char(128)                     |
| last\_name        | char(128)                     |

### ORGANIZATION

| Field             | Description                   |
| ----------------- |:------------------------------|
| name              | require char(128)             |
| description       | require blob                  |
| office            |                               |
| contact\_info     |                               |
| type (?)          |                               |
| etc...            |                               |

### EVENT

| Field             | Description                   |
| ----------------- |:------------------------------|
| name              | required char(128)            |
| description       | required blob                 |
| start\_time       | required datetime             |
| end\_time         | required datetime             |
| location          |                               |
| club\_id          |                               |


## Mappings / Relations

### User to Organization

| Field                | Description                            |
| -------------------- |:---------------------------------------|
| fk\_user\_id         | required foreign key user(id)          |
| fk\_organization\_id | required foreign key organization(id)  |
| admin                | required bool                          |

### Event to Organization (???)

| Field                | Description                            |
| -------------------- |:---------------------------------------|
| fk\_event\_id        | required foreign key event(id)         |
| fk\_organization\_id | required foreign key organization(id)  |

