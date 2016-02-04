# Student gift store

The idea behind this store is to provide a way for parents to buy gifts for students at a private boarding school.
What makes this different from a normal store?
* No shipping
* No revies on products
* Carts limited per students and per parent.
* payment by check allowed
* Admin creates user (Parent adn studant) accounts
* Parents can only buy gifts for related students (related in admin interface)

## Events:
Parents may only buy gifts for specific events. For example birthday and Christmas. Each event has an effective window. There are 2 event types. Personal (birthday) and Holiday (Christmans, New years..). Eligible window, the time before and after an date a gift can be purchased for that event. For exmple, for a Birthday a Parent can buy a gift for 30 day before or 7 days after. For Christmas 60 days before and 7 days after.
* two event types, (personal and Holidays)
* Each event type has a pre and post limit.


## Cart limits:
Cart limits are set per event, per student, per parent. 
For example: 
* If Mike a student has a 3 gift $100 limit. These limits apply to each event, 3 gifts, $100 for Christmas, and another 3 gift $100 for Birthday.
* If a Jill a Parent has a 1 gift $50 Limit and can buy gifts for Mike. Then she can only play 1 gift up to $50 for Christmas and another 1 gift up to $50  as a birthday gift.


