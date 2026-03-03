# Python Flask Application Instrumentation Guide
Follow our [documentation](https://docs.middleware.io/docs/apm-configuration/python/python-apm-setup) to setup APM for your python flask application.

[![PyPI - Version](https://img.shields.io/pypi/v/middleware-io)](https://pypi.org/project/middleware-io/)


Run using:
```
cd misc/github-integration/examples/demo-apm-python-keval/flask
source test_env/bin/activate
pip3 install -r requirements.txt
deactivate


Recent Commits:
b87feb0999ae21f8c63d234910c1f1fb64f82eb8
f2159d30be328b23e94b5d85bb53c9071bd0998d    
75bf0f41d473979beda79e9406d960d887bb8b06
a7ba8abeb9599b6acaab83d4e314108d1860d754
afd91dd6be75d2f53f791dedf7775a281d3633a6
bf4c00cb32f542faac343df6683b5d56ddcac378
ff9989f8febfa4781e749b5891fd09ec066fe6a6
059179d98b8caf620b3a5d82ec820adafe2fdbf9
0141a8bf9635dc6383aa5d0daf5a9eb7fcf82521

1c96e3f6ae748974254c82a14c4f3c615cbd390c stage
75780ce20b1d96d9cf35e9612f6d5fee4a9dd1da stage

df591924d5606e51aa89a2804c356eb4560a5bb9 stage1

demo2:
MW_API_KEY=lneevcqdcnzccpdpbhelkxpjffdxeznkryvb MW_TARGET=https://ruplp.middleware.io:443 MW_SERVICE_NAME=python-beta-sanjay middleware-run flask run

mw-prod:
MW_API_KEY=xusuusalpvush63ud7zcg8bi3mauuptds528 MW_TARGET=https://p2i13hg.middleware.io:443 MW_VCS_COMMIT_SHA=df591924d5606e51aa89a2804c356eb4560a5bb9 MW_VCS_REPOSITORY_URL=https://github.com/temp-mw/demo-apm-python-keval MW_SERVICE_NAME=python-beta-sanjay middleware-run flask run


MW_API_KEY=xusuusalpvush63ud7zcg8bi3mauuptds528 MW_TARGET=https://p2i13hg.middleware.io:443 MW_SERVICE_NAME=python-beta-sanjay-1 middleware-run flask run

MW_API_KEY=5xrocjh0p5ir233mvi34dvl5bepnyqri3rqb MW_TARGET=https://sandbox.middleware.io:443 MW_VCS_COMMIT_SHA=df591924d5606e51aa89a2804c356eb4560a5bb9 MW_VCS_REPOSITORY_URL=https://github.com/temp-mw/demo-apm-python-keval MW_SERVICE_NAME=python-beta-sanjay middleware-run flask run

BETA:
MW_API_KEY=xtzrzvturlisziuvpdffwdsjavkwzpyplwrz MW_TARGET=https://kbuin.beta.env.middleware.io:443 MW_VCS_COMMIT_SHA=df591924d5606e51aa89a2804c356eb4560a5bb9 MW_VCS_REPOSITORY_URL=https://github.com/temp-mw/demo-apm-python-keval MW_SERVICE_NAME=python-beta-sanjay middleware-run flask run
MW_API_KEY=xtzrzvturlisziuvpdffwdsjavkwzpyplwrz MW_TARGET=https://kbuin.beta.env.middleware.io:443 MW_SERVICE_NAME=python-beta-sanjay-1 middleware-run flask run
MW_API_KEY=wohmoeoolifamkcanlhancqbbxtaxznklqyl MW_TARGET=https://izuen.beta.env.middleware.io:443 MW_VCS_COMMIT_SHA=df591924d5606e51aa89a2804c356eb4560a5bb9 MW_VCS_REPOSITORY_URL=https://github.com/temp-mw/demo-apm-python-keval MW_SERVICE_NAME=python-beta-sanjay middleware-run flask run

Local:
MW_API_KEY=xvvviuolicluqilcgchjtqonlfymjtsevzox MW_TARGET=https://911b2386ba0d.ngrok-free.app:443 MW_SERVICE_NAME=python-resource-vcs middleware-run flask run

MW_API_KEY=xvvviuolicluqilcgchjtqonlfymjtsevzox MW_VCS_REPOSITORY_URL=https://github.com/temp-mw/demo-apm-python-keval MW_TARGET=https://b74a-14-195-204-154.ngrok-free.app:443 MW_SERVICE_NAME=python-resource-vcs3 middleware-run flask run

Stage:
MW_API_KEY=mgqjtlgshkyhlykoaermkzbjpmgprkrzmbsb MW_TARGET=https://sbncr.stage.env.middleware.io:443 MW_VCS_COMMIT_SHA=df591924d5606e51aa89a2804c356eb4560a5bb9 MW_VCS_REPOSITORY_URL=https://github.com/temp-mw/demo-apm-python-keval MW_SERVICE_NAME=opsai-py-sanjay middleware-run flask run

MW_API_KEY=mgqjtlgshkyhlykoaermkzbjpmgprkrzmbsb MW_TARGET=https://sbncr.stage.env.middleware.io:443 MW_VCS_REPOSITORY_URL=https://github.com/temp-mw/demo-apm-python-keval MW_VCS_COMMIT_SHA=df591924d5606e51aa89a2804c356eb4560a5bb9 MW_SERVICE_NAME=opsai-py-billing middleware-run flask run

MW_API_KEY=ilfkpyuvjwmuawgvsjjhtbylxinxawwqfqzx MW_TARGET=https://tflmb.stage.env.middleware.io:443 MW_VCS_REPOSITORY_URL=https://github.com/temp-mw/demo-apm-python-keval MW_VCS_COMMIT_SHA=df591924d5606e51aa89a2804c356eb4560a5bb9 MW_SERVICE_NAME=opsai-py-billing middleware-run flask run

MW_VCS_COMMIT_SHA="363326f230cfc9f30fc3a31f85c671ae60d62bcf" MW_VCS_REPOSITORY_URL="https://github.com/temp-mw/demo-apm-python-keval"

MW_API_KEY=mgqjtlgshkyhlykoaermkzbjpmgprkrzmbsb MW_TARGET=https://sbncr.stage.env.middleware.io:443 MW_SERVICE_NAME=opsai-py-sanjay middleware-run flask run

|  Traces  |  Metrics  |  Profiling  |  Logs (App/Custom)  |
|:--------:|:---------:|:-----------:|:-------------------:|
|   Yes    |    Yes    |     Yes     |       Yes/Yes       |

## Prerequisites
Ensure that you have the Middleware Host Agent installed to view Python demo data on your dashboard.

---------------------
## Setup Virtual Environment
```
python -m venv newenv
source newenv/bin/activate

pip install -r requirements.txt
```

## Install Middleware APM package
```shell
pip install middleware-io
```

## Install OpenTelemetry instrument libraries 
```shell
middleware-bootstrap -a install
```

## Run Your Application 

### Option 1 : With Host Agent
To run your application, use the following command:
```shell
middleware-run python app.py
```
### Option 2 : Serverless Setup
```shell
MW_API_KEY=********** MW_TARGET=https://*****.middleware.io:443 middleware-run python app.py
```
---------------------------------
## Run on Docker
1. Build: `docker build -t demo-python .`
2. Run: `docker run demo-python`
3. Debug: `docker run -it demo-python sh`
----------------------------


func (ai *OpsAi) SidePanelReleases(groupId string, fromTsMs, toTsMs int, projectUid string, accountId, projectId int, gitRepositoryUrl, filter string) (aiStore.SidePanelReleasesResponse, error) {
var eventGroupQry string
queryPoints := []interface{}{fromTsMs, toTsMs, groupId, groupId}

	if filter != "" {
		filterData, err := decodeRawBase64ToJSON(filter)
		if err == nil {
			filters := map[string]string{
				"service.name": "t.serviceName",
				"traceID":      "t.traceId",
				"spanID":       "t.spanId",
			}

			for key, column := range filters {
				if value, ok := filterData[key]; ok {
					values := value.(map[string]interface{})["values"].([]interface{})
					if len(values) == 1 {
						eventGroupQry += fmt.Sprintf(" AND %s = ? ", column)
						queryPoints = append(queryPoints, values[0])
					} else {
						eventGroupQry += fmt.Sprintf(" AND %s IN ? ", column)
						queryPoints = append(queryPoints, values)
					}
				}
			}
		}
	}

	q := fmt.Sprintf(`
				SELECT 
			eventGroup,
			COALESCE(commit_sha, 'N/A') AS commit_sha,
			count(*) AS occurrences,
			count(*) * 100.0 / sum(count(*)) OVER (PARTITION BY eventGroup) AS percentage
		FROM 
		(
			SELECT 
				arrayJoin(t.eventsGroupId) AS eventGroup,
				arrayElement(
					arrayElement(t.eventsAttributes, indexOf(t.eventsGroupId, eventGroup)), 
					'exception.vcs.commit_sha'
				) AS raw_commit_sha,
				IF(empty(raw_commit_sha), 'N/A', raw_commit_sha) AS commit_sha
			FROM db_%s.v2_trace_index t
			WHERE 
				t.statusCode = 2
				AND t.timestampNs BETWEEN ? * 1e6 AND ? * 1e6
				AND has(t.eventsGroupId, ?) AND eventGroup = ? %s
		) 
		GROUP BY eventGroup, commit_sha
		ORDER BY occurrences DESC`, projectUid, eventGroupQry)

	//fmt.Println("sidepanel releases--->", q)
	//fmt.Println("sidepanel releases--->", queryPoints)

	var itemResp aiStore.SidePanelReleasesResponse
	itemResp.GroupId = groupId
	itemResp.Attributes = make(map[string][]aiStore.AttrReleasesData)

	chReader := chcluster.CHCluster{Ctx: context.Background(), PuID: projectUid, Stre: ai.Store}.Pool()
	list, err := chReader.Query(q, queryPoints)

	if err != nil {
		mwlogger.Error("Error executing SidePanelData query", "error", err)
		return itemResp, err
	}
	defer list.Close()

	for list.Next() {
		var key, value string
		var occurrences uint64
		var percentage float64
		key = "Release"
		if err := list.Scan(&itemResp.GroupId, &value, &occurrences, &percentage); err != nil {
			mwlogger.Error("Error scanning SidePanelData releases results", "error", err)
			return itemResp, err
		}
		if value == "" {
			continue
		}
		itemResp.Attributes[key] = append(itemResp.Attributes[key], aiStore.AttrReleasesData{
			Value:       value,
			Occurrences: occurrences,
			Percentage:  math.Round(percentage*100) / 100,
		})
	}

	if len(itemResp.Attributes["Release"]) > 0 {
		gitPayloads := integration_endpoint.GithubDetailsPayloads{
			GitRequestedFor:  []string{"sha_releases"},
			GitRepositoryURL: gitRepositoryUrl,
		}
		isError, resp := ai.Endpoints.Integration.FetchGitHubDataset(context.Background(), accountId, projectId, gitPayloads)

		if isError || resp.Status != true {
			mwlogger.Error("FetchGitHubDataset failed", "error", isError, "message", resp.Message)
			return itemResp, errors.New(resp.Message)
		}

		if resp.Details == nil {
			mwlogger.Error("FetchGitHubDataset response missing 'details'")
			return itemResp, errors.New("missing 'details' in FetchGitHubDataset response")
		}

		shaReleasesRaw, exists := resp.Details["sha_releases"]
		if !exists {
			mwlogger.Error("'sha_releases' not found in response details")
			return itemResp, errors.New("'sha_releases' key missing in response details")
		}

		//fmt.Println("Raw sha_releases Data:")
		//utils.PrintJSon(shaReleasesRaw)

		shaReleasesMap, isMap := shaReleasesRaw.(map[string][]map[string]string)
		if !isMap {
			mwlogger.Error("Invalid format for 'sha_releases'", "expected", "map[string][]map[string]string", "got", reflect.TypeOf(shaReleasesRaw))
			return itemResp, errors.New("invalid format for 'sha_releases'")
		}

		for i, attr := range itemResp.Attributes["Release"] {
			releaseList := make([]aiStore.AttrReleasesListData, 0)

			// Check if SHA exists in response
			if shaData, exists := shaReleasesMap[attr.Value]; exists {
				for _, releaseItem := range shaData {
					if len(releaseItem) > 0 {
						release := aiStore.AttrReleasesListData{
							Label:      "N/A",
							ReleaseURL: "",
						}

						if r, ok := releaseItem["release"]; ok {
							shaInitials := getSHAInitials(attr.Value)
							release.Label = fmt.Sprintf("%s (%s)", r, shaInitials)
						}
						if url, ok := releaseItem["html_url"]; ok {
							release.ReleaseURL = url
						}

						releaseList = append(releaseList, release)
					}
				}
			}

			if len(releaseList) == 0 {
				if attr.Value == "N/A" {
					releaseList = append(releaseList, aiStore.AttrReleasesListData{
						Label:      "N/A (empty)",
						ReleaseURL: "",
					})
				} else {
					shaInitials := getSHAInitials(attr.Value)
					releaseList = append(releaseList, aiStore.AttrReleasesListData{
						Label:      fmt.Sprintf("N/A (%s)", shaInitials),
						ReleaseURL: "",
					})
				}

			}

			updatedAttr := aiStore.AttrReleasesData{
				Value:       attr.Value,
				Occurrences: attr.Occurrences,
				Percentage:  attr.Percentage,
				Releases:    releaseList,
			}
			itemResp.Attributes["Release"][i] = updatedAttr
		}

		//fmt.Println("Updated Response:")
		//utils.PrintJSon(itemResp)
	}

	return itemResp, nil
}