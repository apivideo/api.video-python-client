# Player

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**text** | **str** | RGBA color for timer text. Default: rgba(255, 255, 255, 1) | [optional] 
**link** | **str** | RGBA color for all controls. Default: rgba(255, 255, 255, 1) | [optional] 
**link_hover** | **str** | RGBA color for all controls when hovered. Default: rgba(255, 255, 255, 1) | [optional] 
**track_played** | **str** | RGBA color playback bar: played content. Default: rgba(88, 131, 255, .95) | [optional] 
**track_unplayed** | **str** | RGBA color playback bar: downloaded but unplayed (buffered) content. Default: rgba(255, 255, 255, .35) | [optional] 
**track_background** | **str** | RGBA color playback bar: background. Default: rgba(255, 255, 255, .2) | [optional] 
**background_top** | **str** | RGBA color: top 50% of background. Default: rgba(0, 0, 0, .7) | [optional] 
**background_bottom** | **str** | RGBA color: bottom 50% of background. Default: rgba(0, 0, 0, .7) | [optional] 
**background_text** | **str** | RGBA color for title text. Default: rgba(255, 255, 255, 1) | [optional] 
**enable_api** | **bool** | enable/disable player SDK access. Default: true | [optional]  if omitted the server will use the default value of True
**enable_controls** | **bool** | enable/disable player controls. Default: true | [optional]  if omitted the server will use the default value of True
**force_autoplay** | **bool** | enable/disable player autoplay. Default: false | [optional]  if omitted the server will use the default value of False
**hide_title** | **bool** | enable/disable title. Default: false | [optional]  if omitted the server will use the default value of False
**force_loop** | **bool** | enable/disable looping. Default: false | [optional]  if omitted the server will use the default value of False
**player_id** | **str** |  | [optional] 
**created_at** | **datetime** | When the player was created, presented in ISO-8601 format. | [optional] 
**updated_at** | **datetime** | When the player was last updated, presented in ISO-8601 format. | [optional] 
**shape_margin** | **int** | Deprecated | [optional] 
**shape_radius** | **int** | Deprecated | [optional] 
**shape_aspect** | **str** | Deprecated | [optional] 
**shape_background_top** | **str** | Deprecated | [optional] 
**shape_background_bottom** | **str** | Deprecated | [optional] 
**link_active** | **str** | Deprecated | [optional] 
**assets** | [**PlayerAllOfAssets**](PlayerAllOfAssets.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


