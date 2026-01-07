## NoSQL Database Analysis – FLEXIMART

## Section A: Limitations of RDBMS

Relational databases like MySQL work well for structured and fixed data models, but they face several limitations when handling highly diverse and dynamic product information. In FLEXIMART, different product categories have different attributes. For example, laptops require specifications such as RAM, processor, storage, and battery, while shoes require size, color, and material. In an RDBMS, supporting this variation would require many nullable columns or multiple additional tables, making the schema complex, inefficient, and harder to maintain.

Another challenge is frequent schema changes. Whenever a new product type is introduced, the relational schema must be altered using ALTER TABLE commands. These changes can cause downtime, increase maintenance effort, and slow down development cycles. Managing continuously evolving schemas becomes increasingly difficult as the product catalog grows in size and complexity.

Storing customer reviews is also problematic in relational databases. Reviews require multiple related tables and joins to store ratings, comments, and review dates. This increases query complexity and negatively impacts performance when fetching complete product details along with customer reviews.

## Section B: Benefits of MongoDB

MongoDB addresses these issues by using a flexible, schema-less document model. Each product is stored as a document, allowing different products to have different fields without enforcing a fixed structure. Laptops, shoes, and groceries can store their specific attributes independently, making the system highly adaptable to changing business requirements.

MongoDB supports embedded documents, which allows customer reviews to be stored directly inside the product document. Ratings, comments, and review dates can be retrieved in a single query, improving performance, reducing query complexity, and simplifying application-level data access.

Additionally, MongoDB supports horizontal scalability through sharding. As FlexiMart’s product catalog, customer base, and traffic grow, data can be distributed across multiple servers, ensuring high availability, fault tolerance, and better performance for large-scale e-commerce applications.

## Section C: Trade-offs of Using MongoDB

Although MongoDB offers many advantages, it also has some disadvantages when compared to relational databases. One limitation is its weaker support for complex transactions that involve multiple documents across collections. While MongoDB supports multi-document transactions, they are often harder to implement and may perform slower than transactions in relational databases such as MySQL.

Another drawback is that MongoDB does not strictly enforce schemas or relational constraints like foreign keys. As a result, data consistency and integrity must be managed at the application level. For systems that require strict schemas, strong data integrity, and complex relational queries, MySQL can still be a more reliable and suitable choice.






