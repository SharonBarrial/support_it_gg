""""
1. Question:
Which of the following is not an advantage of replication of data in terms of directory services?
It allows local management of user accounts.
🔹 Explanation: Replication helps with redundancy, lower latency, and local access — but flexibility for new object types is a schema feature, not a replication advantage.

2. Question:
Which directory service software would be used exclusively on a Windows network?
✅ Answer: Active Directory
🔹 Explanation: Active Directory is Microsoft’s proprietary directory service.

3. Question:
Which of these are advantages of centralized management using directory services? (Choose all that apply)
✅ Answers:

Role-Based Access Control (RBAC) can organize user groups centrally.

Access and authorization are managed in one place.

Configuration management is centralized.
🔸 "Configuration can take place on each device" is incorrect because it's the opposite of centralized management.

4. Question:
What is the organizational unit of this entry?
✅ Answer: Sysadmin
🔹 Explanation: The "OU=" part defines the Organizational Unit.

5. Question:
Which of the following are ways to authenticate to an LDAP server? (Choose all that apply)
✅ Answers:

Simple bind

SASL

Anonymous bind
🔸 PGP is not an LDAP authentication method.

6. Question:
Which of these statements about Active Directory (AD) are true? (Choose all that apply)
✅ Answers:

AD can "speak" LDAP.
AD is used as a central repository of group policy objects, or GPOs.

7. Question:
If a system administrator needs to give access to a resource to everyone in a domain, what group in Active Directory can they use?
✅ Answer: Domain Users
🔹 Explanation: "Domain Users" includes all users in the domain by default.

8. Question:
To authenticate user accounts on a computer against AD, what must be done to the computer first?
✅ Answer: Join it to the domain
🔹 Explanation: A computer must be part of the domain to use AD for authentication.

9. Question:
What is the difference between a group policy and a group policy preference?
✅ Answer: Policies are reapplied every 90 minutes, and preferences are a settings template that the user can change on the computer.
🔹 Explanation: Policies enforce rules; preferences suggest settings that users can override.

10. Question:
You'd like to change the minimum password length policy in the Default Domain Policy group policy preference (GPO). What's the best way to go about doing this?
✅ Answer: Open the Group Policy Management Console by running gpmc.msc from the CLI
🔹 Explanation: GPMC is the standard tool for managing Group Policy.
Question 6
In Active Directory, which of the following can be functions of the Domain? (Choose all that apply)

A server that holds a replica of the Active Directory database
Correct

A DNS server
Correct

A Kerberos authentication server
Correct

A container X 
This should not be selected

Question 3
Instead of assigning access for each user account individually, ________ is a more efficient and easier-to-manage approach.

active directory x
centralized authentication X
centralized management*
LDAP

*Which of the following is not an advantage of replication of data in terms of directory services?

It decreases latency when accessing the directory service.
It allows flexibility, allowing for easy creation of new object types as needs change. X
It allows local management of user accounts.*
It provides redundancy for data.

*Which of these statements about Active Directory (AD) are true? (Choose all that apply)
AD includes a tool called the Active Directory Authentication Center, or ADAC. x
AD is incompatible with Linux, OS X, and other non-Windows hosts.
AD can "speak" LDAP.*
AD is used as a central repository of group policy objects, or GPOs.*

""""
