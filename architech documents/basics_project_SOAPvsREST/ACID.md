## ACID Properties

ACID is an acronym for the four key properties of database transactions that ensure reliability and integrity. These properties are:

| Property    | Description                                                                                                                                              | Example                                                                                                                                                                   |
|-------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Atomicity**   | A transaction is treated as a single unit. Either all operations within the transaction are completed, or none of them are.                            | In a banking system, transferring money from Account A to Account B involves debiting Account A and crediting Account B. If one fails, the transaction is rolled back.  |
| **Consistency** | A transaction ensures that the database transitions from one valid state to another while adhering to all rules and constraints.                      | A database rule prevents account balances from being negative. If a transaction violates this rule, it fails, leaving the database consistent.                          |
| **Isolation**   | Transactions execute independently. Partial effects of one transaction are not visible to others until the transaction is complete.                  | In an e-commerce system, two users attempting to buy the last item won't see inconsistent inventory counts due to proper transaction isolation.                          |
| **Durability**   | Once a transaction is successfully completed, its results are permanently recorded in the database, even in the event of a system crash.              | After booking a flight ticket, the confirmation persists in the system, even if the server crashes right afterward.                                                     |

### ACID in Microservices
- **Challenge**: Strict ACID compliance is difficult in microservices because they often use distributed databases.
- **Approaches**:
  - **Eventual Consistency**: Many microservices trade strict ACID compliance for eventual consistency to ensure scalability and performance.
  - **Transaction Managers**: Tools like **Sagas** and **Distributed Transactions** help maintain consistency across multiple services.
