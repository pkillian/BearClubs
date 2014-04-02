/*
    In this view, we create a subscription object structure to return, select
    all items that are related to the User via the associated mappings 
    (UserToOrganization, UserToEvent, etc.), and include logical indications
    in the subscription object to descirbe what type of object the row in the
    return data is.

    For example, if User1 has two subscriptions, Org1 and Event1, the return
    data should be of a form similar to:

    ```
    SELECT * FROM bc_user_subscription_view WHERE username = 'User1';

    Field                           | Data
    -----------------------------------------------------------------
    user_id                         | 1
    user_username                   | 'User1'
    ...                             | ...
    subscription_type               | 0
    subscription_type_description   | 'Organization'
    subscription_id                 | 1
    subscription_name               | 'Org1'
    ...                             | ...
    -----------------------------------------------------------------
    user_id                         | 1
    user_username                   | 'User1'
    ...                             | ...
    subscription_type               | 1
    subscription_type_description   | 'Event'
    subscription_id                 | 1
    subscription_name               | 'Event1'
    ...                             | ...
    
    ```

    This return data should encapsulate all possible commonalities between
    object types. The calling section of code ideally should NOT have to make
    further calls to the DB to get more data; this adds unnessecary I/O. 

*/

-- Create return data structure here

-- DROP IF EXISTS bc_user_subscription_view;

/* 
CREATE VIEW bc_user_subscription_view AS

    SELECT INTO `return data structure name` 
    FROM bc_user_to_organization 
    WHERE user_id = `user id variable`;

    SELECT INTO `return data structure name` 
    FROM bc_user_to_event
    WHERE user_id = `user id variable`;
;
*/
 
CREATE VIEW bc_user_subscription_view AS

    SELECT * FROM bc_user_to_organization 
        INNER JOIN bc_user_to_event ON (bc_user_to_organization.user_id = bc_user_to_event.user_id)
;
