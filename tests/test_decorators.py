from bitbucket_webhooks_router import decorators


@decorators.handle_repo_push
def sample_repo_push_handler_1(num):
    return 1


@decorators.handle_repo_push
def sample_repo_push_handler_2(num):
    return 2


@decorators.handle_pr_approval
def sample_pr_approval_handler(num):
    return 3


def test_handlers():
    assert len(decorators.handle_repo_push.methods) == 2
    results = [method(9) for method in decorators.handle_repo_push.methods]
    assert results == [1, 2]

    assert len(decorators.handle_pr_approval.methods) == 1
    results = [method(9) for method in decorators.handle_pr_approval.methods]
    assert results == [3]
