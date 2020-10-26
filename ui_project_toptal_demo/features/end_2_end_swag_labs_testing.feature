Feature: End to end automated testing in Swag labs e-commerce test page
	As QA Front End automation engineer
	I want to show some automated test cases
	Applied to test page: "https://www.saucedemo.com/inventory.html"
	So I can demonstrate my automation skills for FE
	Using behave as BDD testing framework
	
	Scenario: Basic login process
	Given the swag labs page is displayed
	When I write the username and password
	And I click on login Button
	Then I will see the home page of swag labs displayed

	Scenario: Add item to shopping cart
	Given I click on the first add to cart button
	When I click on the shopping cart
	Then I noticed that one package was added

	Scenario: Add second item to shopping cart
	Given I am on the home page
	And I click on the second item to add to cart button
	When I click on the shopping cart
	Then I noticed that second package was added 

	Scenario: Remove item from shopping cart
	Given I am on shopping cart page
	When I click on remove button
	Then I noticed that the item was removed

	Scenario: Sort product list from Z to A
	Given I am on the home page
	When I click on sort button
	And select the option Z to A
	Then I noticed that item list is sorted 

	Scenario: Sort product list Price low to high
	Given I am on the home page
	When I click on sort button
	And select the option low to high
	Then I noticed that item list is sorted low to high

	Scenario: Sort product list Price high to low
	Given I am on the home page
	When I click on sort button
	And select the option high to low
	Then I noticed that item list is sorted high to low

	Scenario: checkout product in the shopping cart
	Given I go to shopping cart page
	When I click on checkout button
	Then I noticed 3 fields displayed
	When I filled then up
	And I click on continue button
	Then I overview the order
	When I click on finish button
	Then I noticed that order was dispatched

	Scenario: Logout from the app
	Given I am on the home page
	When I click on the left principal menu
	And click on Logout button
	Then Login page is displayed
