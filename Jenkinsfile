pipeline {
  agent any
  environment {
    commit_sha = "" 
  }
  stages {
    stage("Get Commit SHA") {
      script {
        def commitHashForBuild(build) {
            def scmAction = build?.actions.find { action -> action instanceof jenkins.scm.api.SCMRevisionAction }
            if (scmAction?.revision instanceof org.jenkinsci.plugins.github_branch_source.PullRequestSCMRevision) {
                return scmAction?.revision?.pullHash
            } else if (scmAction?.revision instanceof jenkins.plugins.git.AbstractGitSCMSource$SCMRevisionImpl) {
                return scmAction?.revision?.hash
            } else {
                error("Build doesn't contain revision information. Do you run this from GitHub organization folder?")
            }
        }

        commit_sha = commitHashForBuild(currentBuild.rawBuild) 
      }
    }
    stage("print") {
      steps {
        echo "${commit_sha}"
      }
    }
  }
}
