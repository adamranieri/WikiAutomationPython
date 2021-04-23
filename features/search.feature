Feature: Search

  Scenario Outline: Searching Keywords
    Given The Guest is on the Wikipedia Home Page
    When The Guest types <word> in the search bar
    When The Guest clicks the search button
    Then The title should be <title>

    Examples:
      | word | title |
      | West Virginia | West Virginia - Wikipedia |
      | Florida | Florida - Wikipedia |
      | New Jersey | New Jersey - Wikipedia |