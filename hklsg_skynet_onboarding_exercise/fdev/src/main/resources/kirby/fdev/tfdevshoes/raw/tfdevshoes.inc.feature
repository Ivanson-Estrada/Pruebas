@fdev
Feature: Tests for tfdevshoes in fdev

  @execute
  Scenario: tfdevshoes-raw-inc
    Given an ingestion config file ${repository.endpoint}/${repository.repo}/kirby/mx/fdev/raw/tfdevshoes/${version}/tfdevshoes.inc.conf
    When I read input as dataframe with info
      | dateColumn  | dataDate  | executionDate | sender  | dataSourceId  | objectPath  |  physicalObjectName  |  frequency  |
      |             |           |               |         |               |             |                      |             |
    And I read output as dataframe with info
      | dateColumn  | dataDate  | executionDate | sender  | dataSourceId  | objectPath  |  physicalObjectName  |  frequency  |
      |             |           |               |         |               |             |                      |             |
    Then output dataframe is not empty with thresholds (100.0, 100.0)
    And output dataframe has the same records than input dataframe with thresholds (100.0, 100.0)
    And the number of columns for output dataframe are equal to the number of columns for input dataframe
    And output partitions have less than 100 files per directory
    And average for output file size are greater than 128 MB
    And output dataframe does not have null values for columns with thresholds (100.0, 100.0)
      | column name           |
    And records for output dataframe have the format ^[a-zA-Z]+$ for columns with thresholds (100.0, 100.0)
      | column name           |

