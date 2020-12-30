'''
Enhancing database security


Recently, several inconsistencies have been discovered on the Fresh Fruit Delivery company's database server.

The IT Security team does not have an auditing process to find out when users are connecting to the database and track breaking changes back to the responsible user.

You are asked to help the Security team by implementing a new trigger based on their requirements.

Due to the complexity of this request, you should build the INSERT statement in the first step and use it to create the trigger in the second step.

Instructions 1/2
50 XP

- Create the INSERT statement that is going to fill in user details in the ServerLogonLog table.
- Select only the details for the situation when the session_id is the same as the @@SPID (ID of the current user).

'''
-- Save user details in the audit table
INSERT INTO ServerLogonLog(LoginName, LoginDate, SessionID, SourceIPAddress)
SELECT ORIGINAL_LOGIN(), GETDATE(), @@SPID, client_net_address

-- The user details can be found in SYS.DM_EXEC_CONNECTIONS
FROM SYS.DM_EXEC_CONNECTIONS WHERE session_id = @@SPID


'''
Instructions 2/2
50 XP

- Create a new trigger at the server level that fires for logon events and saves user details into ServerLogonLog table.

'''

-- Create a trigger firing when users log on to the server
CREATE TRIGGER LogonAudit
-- Use ALL SERVER to create a server-level trigger
ON ALL SERVER WITH EXECUTE AS 'sa'
-- The trigger should fire after a logon
FOR LOGON
AS
-- Save user details in the audit table
INSERT INTO ServerLogonLog(LoginName, LoginDate, SessionID, SourceIPAddress)
SELECT ORIGINAL_LOGIN(), GETDATE(), @@SPID, client_net_address
FROM SYS.DM_EXEC_CONNECTIONS WHERE session_id = @@SPID
