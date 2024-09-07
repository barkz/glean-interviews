# ClientConfig
## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Assistant** | [**AssistantConfig**](AssistantConfig.md) |  | [optional] 
**Tools** | [**ToolsConfig**](ToolsConfig.md) |  | [optional] 
**Shortcuts** | [**ShortcutsConfig**](ShortcutsConfig.md) |  | [optional] 
**BadVersions** | **String[]** | Known bad client versions that should force update themselves | [optional] 
**FeedPeopleCelebrationsEnabled** | **Boolean** | Whether people celebrations is enabled or not for the instance | [optional] 
**FeedSuggestedEnabled** | **Boolean** | Whether the suggested feed is enabled | [optional] 
**FeedTrendingEnabled** | **Boolean** | Whether the trending feed is enabled | [optional] 
**FeedRecentsEnabled** | **Boolean** | Whether the recents feed is enabled | [optional] 
**FeedMentionsEnabled** | **Boolean** | Whether the mentions feed is enabled | [optional] 
**GptAgentEnabled** | **Boolean** | Whether the GPT agent for Chat is enabled | [optional] 
**ChatHistoryEnabled** | **Boolean** | Whether the chat history for Chat is enabled | [optional] 
**BoolValues** | **System.Collections.Hashtable** | A map of {string, boolean} pairs representing flags that globally guard conditional features. Omitted flags mean the client should use its default state. | [optional] 
**IntegerValues** | **System.Collections.Hashtable** | A map of {string, integer} pairs for client consumption. | [optional] 
**CompanyDisplayName** | **String** | The user-facing name of the company owning the deployment | [optional] 
**CustomSerpMarkdown** | **String** | A markdown string to be displayed on the search results page. Useful for outlinks to help pages. | [optional] 
**OnboardingQuery** | **String** | A demonstrative query to show during new user onboarding | [optional] 
**IsOrgChartLinkVisible** | **Boolean** | Determines whether the org chart link in the Directory panel is visible to all users. | [optional] 
**IsOrgChartAccessible** | **Boolean** | Determines whether the org chart is accessible to all users, regardless of link visibility. Org chart can be accessible even if the org chart link in Directory is not visible. | [optional] 
**IsPeopleSetup** | **Boolean** | Whether or not people data has been set up. | [optional] 
**IsPilotMode** | **Boolean** | Whether or not the deployment is in pilot mode. | [optional] 
**WebAppUrl** | **String** | URL the company uses to access the web app | [optional] 
**UserOutreach** | [**UserOutreachConfig**](UserOutreachConfig.md) |  | [optional] 
**SearchLinkUrlTemplate** | **String** | The URL to use for outbound links to Glean Search. Defaults to {webAppUrl}/search?q&#x3D;%s. | [optional] 
**ChatLinkUrlTemplate** | **String** | The URL to use for outbound links to Glean Chat. Defaults to {webAppUrl}/chat. | [optional] 
**Themes** | [**Themes**](Themes.md) |  | [optional] 
**Brandings** | [**ClientConfigBrandings**](ClientConfigBrandings.md) |  | [optional] 
**GreetingFormat** | **String** | Describes how to format the web app greeting. Possible format options include \%t - timely greeting \%n - the user&#39;s first name | [optional] 
**TaskSeeAllLabel** | **String** | Label for the external link at the end of the Task card in order to guide user to the source. | [optional] 
**TaskSeeAllLink** | **String** | Link used in conjunction with taskSeeAllLabel to redirect user to the task&#39;s source. | [optional] 
**ShortcutsPrefix** | **String** | Company-wide custom prefix for Go Links. | [optional] 
**SsoCompanyProvider** | **String** | SSO provider used by the company | [optional] 
**FeedbackCustomizations** | [**FeedbackCustomizations**](FeedbackCustomizations.md) |  | [optional] 

## Examples

- Prepare the resource
```powershell
$ClientConfig = Initialize-PSOpenAPIToolsClientConfig  -Assistant null `
 -Tools null `
 -Shortcuts null `
 -BadVersions null `
 -FeedPeopleCelebrationsEnabled null `
 -FeedSuggestedEnabled null `
 -FeedTrendingEnabled null `
 -FeedRecentsEnabled null `
 -FeedMentionsEnabled null `
 -GptAgentEnabled null `
 -ChatHistoryEnabled null `
 -BoolValues null `
 -IntegerValues {&quot;autocompleteDebounceMs&quot;:300,&quot;retries&quot;:3} `
 -CompanyDisplayName null `
 -CustomSerpMarkdown null `
 -OnboardingQuery null `
 -IsOrgChartLinkVisible null `
 -IsOrgChartAccessible null `
 -IsPeopleSetup null `
 -IsPilotMode null `
 -WebAppUrl null `
 -UserOutreach null `
 -SearchLinkUrlTemplate null `
 -ChatLinkUrlTemplate null `
 -Themes null `
 -Brandings null `
 -GreetingFormat \%t, \%n (This would be the current default Glean greeting) `
 -TaskSeeAllLabel null `
 -TaskSeeAllLink null `
 -ShortcutsPrefix null `
 -SsoCompanyProvider null `
 -FeedbackCustomizations null
```

- Convert the resource to JSON
```powershell
$ClientConfig | ConvertTo-JSON
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

