# Exercise 2

## Business Process Description

Star model for youth program members within the Brooklyn location

## Fact Table
Transaction table
| Column Name | Type | Description |
| --- | --- | --- |
| transactId | bigint | transaction id |
| amount | float | amount references how much was transactioned |
| transactionType | nvarchar(20) | references type of tranaction |
| accountId | bigint | accountId referencing account |
| gymId | int | gym id to reference gym location |
| timestamp | datetime | date and time when transaction occurred|
| youthId | bigint | referencing whether customer is associated with a youth |
## Dimension
**Customer table**
| Column Name | Type | Description |
| --- | --- | --- |
| accountId | bigint | fk referencing customer account from transaction table |
| name | nvarchar(100) | references customer name associated with account |
| age | tinyint | references age of customer |
| email | nvarchar(30) | email of customer |
| youth | bigint |boolean referencing whether customer is associated with a youth |
Youth Table
| accountId | bigint | fk referencing customer account from transaction table |
| youthId | bigint | referencing whether customer is associated with a youth |
| YouthProgram | bit | indicating if they're a part of youth program |


**YouthProgram** table
| Column Name | Type | Description |
| --- | --- | --- |
| youthId | bigint | id of youth in youth program |
| memberSince | datetime | when youth became a member |
| name | nvarchar(100) | referencing youth name |
| YouthTeam |  Array |  what team or teams they are a part of | 
| SummerCamp | bit | are they participating in this years summer camp |

**SummerCamp** table
| Column Name | Type | Description |
| --- | --- | --- |
| youthId | bigint | id of youth in youth program |
| YouthTeam | Array | what teams are the in |
| Year | int | what year are they participating in | 


