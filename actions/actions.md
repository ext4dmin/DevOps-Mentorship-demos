# GitHub Events Overview

## check_run
- **Types:** created, completed, rerequested
- **Context:** Useful for integration with CI/CD systems. For example, when code is pushed, the CI system runs tests, and upon completion, the `completed` event is triggered.
  
## check_suite
- **Types:** completed, requested, rerequested
- **Context:** Convenient for managing a whole suite of checks. For instance, if a review of all checks is requested after changes, the `rerequested` event will be activated.

## create
- **Types:** branch, tag
- **Context:** Triggered when new branches or tags are created. For example, creating a new branch `feature/awesome-feature` will trigger a `create` event with type `branch`.

## delete
- **Types:** branch, tag
- **Context:** Triggered when branches or tags are deleted. For example, deleting the branch `old-feature` will trigger a `delete` event with type `branch`.

## deployment
- **Types:** created
- **Context:** Tracking application deployments. For example, deploying a new version of a web application.

## deployment_status
- **Types:** created
- **Context:** Monitoring deployment status. For example, whether a deployment was successful or failed.

## discussion
- **Types:** created, deleted, edited, pinned, unpinned, locked, unlocked, transferred
- **Context:** Useful for team collaboration and discussions. For example, creating a new discussion about a new feature.

## discussion_comment
- **Types:** created, deleted, edited
- **Context:** Monitoring comments in discussions. For example, leaving a comment in a discussion.

## fork
- **Types:** created
- **Context:** Tracking who forks your repository. For example, someone forks your repository to make their changes.

## gollum
- **Types:** page_created, page_edited
- **Context:** Updates to wiki pages. For example, adding a new documentation page or editing an existing one.

## issue_comment
- **Types:** created, edited, deleted
- **Context:** Working with comments in issues and pull requests. For example, leaving a comment suggesting improvements to an issue.

## issues
- **Types:** opened, edited, deleted, transferred, pinned, unpinned, closed, reopened, assigned, unassigned, labeled, unlabeled, locked, unlocked, milestone, demilestoned
- **Context:** Managing issues. For example, opening a new issue, assigning a responsible person, and adding a label.

## label
- **Types:** created, edited, deleted
- **Context:** Managing labels. For example, creating a new label "bug" and adding it to an issue.

## merge_group
- **Types:** created, updated
- **Context:** Merging multiple pull requests. For example, creating a group for simultaneously merging several pull requests.

## milestone
- **Types:** created, closed, opened, edited
- **Context:** Tracking key project milestones. For example, creating a new milestone "Version 1.0" and closing it after completing all tasks.

## page_build
- **Types:** created
- **Context:** Building and rebuilding GitHub Pages sites. For example, updating documentation and rebuilding the site.

## project
- **Types:** created, updated, closed, reopened, edited
- **Context:** Managing projects. For example, creating a new project "Refactor Backend".

## project_card
- **Types:** created, moved, converted, edited, deleted
- **Context:** Managing task cards in a project. For example, moving a task card from "To Do" to "In Progress".

## project_column
- **Types:** created, updated, moved, deleted
- **Context:** Managing columns in a project. For example, creating a new column "Testing" for tasks.

## public
- **Types:** repository_publicized
- **Context:** Making a repository public. For example, changing a private repository to public.

## pull_request
- **Types:** assigned, unassigned, labeled, unlabeled, opened, edited, closed, reopened, synchronize, ready_for_review, locked, unlocked, review_requested, review_request_removed, converted_to_draft
- **Context:** Managing pull requests. For example, creating a new pull request and assigning it for review.

## pull_request_comment
- **Types:** (use issue_comment)
- **Context:** Commenting on a pull request via `issue_comment`. For example, leaving a note on changes in a pull request.

## pull_request_review
- **Types:** submitted, edited, dismissed
- **Context:** Working with reviews on pull requests. For example, leaving a detailed review on a pull request.

## pull_request_review_comment
- **Types:** created, edited, deleted
- **Context:** Commenting within a pull request review. For example, adding a comment to a specific line of code in a pull request.

## pull_request_target
- **Types:** assigned, unassigned, labeled, unlabeled, opened, edited, closed, reopened, synchronize, ready_for_review, locked, unlocked, review_requested, review_request_removed, converted_to_draft
- **Context:** Similar to `pull_request`, but for the base repository. For example, a request to change code that is executed in the context of the base repository.

## push
- **Types:** branch, tag
- **Context:** Tracking changes in the repository. For example, pushing new commits to the `master` branch.

## registry_package
- **Types:** published, updated
- **Context:** Managing packages in GitHub Packages. For example, publishing a new version of a package.

## release
- **Types:** published, edited, deleted
- **Context:** Managing project releases. For example, publishing version 1.0.0 of your application.

## repository_dispatch
- **Types:** created
- **Context:** Triggering actions via external API. For example, a third party initiates an event to run a script in your repository.

## schedule
- **Types:** (cron syntax)
- **Context:** Regular tasks on a schedule. For example, a daily dependency check in the project at 00:00.

## status
- **Types:** (depends on commit status)
- **Context:** Updating commit status. For example, changing the build status of a commit to successful or failed.

## watch
- **Types:** starred
- **Context:** Tracking stars added to repositories. For example, a user stars your repository.

## workflow_call
- **Types:** created
- **Context:** Calling one workflow from another. For example, one workflow calls another to perform a specific task.

## workflow_dispatch
- **Types:** (manual)
- **Context:** Manual triggering of a workflow through the GitHub interface. For example, manually starting a build and test of the project.

## workflow_run
- **Types:** requested, completed
- **Context:**

```yaml
name: Multi-Stage CI/CD

on: 
  push:
    branches:
      - main
  pull_request:
    branches:
      - main

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout code
        uses: actions/checkout@v2
        
      - name: Build project
        run: |
          echo "Building the project..."
          # Ваши команды сборки

  test:
    runs-on: ubuntu-latest
    needs: build
    steps:
      - name: Checkout code
        uses: actions/checkout@v2
        
      - name: Run tests
        run: |
          echo "Running tests..."
          # Ваши команды тестирования

  deploy:
    runs-on: ubuntu-latest
    needs: test
    steps:
      - name: Checkout code
        uses: actions/checkout@v2
        
      - name: Deploy to server
        run: |
          echo "Deploying to server..."
          # Ваши команды деплоя
```

# GitHub variables

1. **github.event_name**: Имя события, которое запустило workflow (например, `push`, `pull_request`).
   * _Primer_: `github.event_name == 'push'`

2. **github.ref**: Ссылка на ветку или тег, в которой произошло событие (например, `refs/heads/main`).
   * _Primer_: `github.ref == 'refs/heads/main'`

3. **github.sha**: SHA коммита, который запустил workflow.
   * _Primer_: `github.sha == '1a2b3c4d'`

4. **github.repository**: Полное название репозитория (например, `owner/repo`).
   * _Primer_: `github.repository == 'myuser/myrepo'`

5. **github.actor**: Имя пользователя, вызвавшего событие (например, `myuser`).
   * _Primer_: `github.actor == 'myuser'`

6. **github.workflow**: Имя workflow, который выполняется.
   * _Primer_: `github.workflow == 'CI/CD Workflow'`

7. **github.action**: Имя действия, которое выполняется.
   * _Primer_: `github.action == 'deploy'`

8. **github.event**: Полный JSON объект события, инициировавшего workflow.
   * _Primer_: `github.event.issue.number == 1` (для событий типа issues)

9. **github.job**: Имя текущей задачи.
   * _Primer_: `github.job == 'build'`

10. **github.run_id**: Уникальный идентификатор текущего запуска workflow.
    * _Primer_: `github.run_id == '123456789'`

11. **github.run_number**: Номер текущего запуска workflow.
    * _Primer_: `github.run_number == '42'`

12. **github.repository_owner**: Владелец репозитория.
    * _Primer_: `github.repository_owner == 'myuser'`

13. **github.head_ref**: Ветка, которая была создана в пулл-реквесте (PR).
    * _Primer_: `github.head_ref == 'feature-branch'`

14. **github.base_ref**: Базовая ветка, в которую был создан пулл-реквест (PR).
    * _Primer_: `github.base_ref == 'main'`

15. **github.token**: Токен для аутентификации, используемый действиями для взаимодействия с GitHub API.
    * _Primer_: `github.token == 'ghp_abcdefghijklmnopqrstuvwxyz'`
