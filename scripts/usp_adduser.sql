SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
-- =============================================
-- Author:		<Author,,Samir>
-- Create date: <2019-12-05,,>
-- Description:	<New user insertion sp,,>
-- =============================================
CREATE PROCEDURE UDSP_Add_user
	-- Add the parameters for the stored procedure here
	 @FirstName varchar(50),
	 @LName varchar(50), 
	 @Email varchar(50)
	 --@Role_id int
	
As
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

    -- Insert statements for procedure here
	Insert into DMS_adduser (FirstName,LastName,Email)--,Role_id)   
           Values (@FirstName,@LName, @Email)--,@Role_id)
END
GO

