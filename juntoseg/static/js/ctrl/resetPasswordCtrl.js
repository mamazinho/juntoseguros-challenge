challenge.controller('ResetPasswordCtrl', function($scope, HttpFctr){

    $scope.__init__ = function(){
      $scope.email = ''
      $scope.showResetModal = false
      $scope.seeToken = false
      $scope.myTokenReset = ''
      $scope.showChangePassword = false
      $scope.changePassword = {
        'email': '',
        'token': '',
        'password': '',
        'confirmPassword': ''
      }
    }

    $scope.reset = () => {
      HttpFctr('reset-password', 'POST', {data: {email: $scope.email}})
      .then((response) => {
        $scope.myTokenReset = response.token
        $scope.showResetModal = true
      }).catch((error) => {
        console.log('Error >> ', error)
        alert(window.errorMessage)
      })
    }
  
    $scope.change = () => {
      $scope.changePassword.email = $scope.email
      $scope.changePassword.token = $scope.myTokenReset
      HttpFctr('change-password', 'PATCH', {data: $scope.changePassword})
      .then((response) => {
        alert(response.success)
        $scope.$emit('changeTab', 'login')
      }).catch((error) => {
        console.log('Error >> ', error)
        alert(window.errorMessage)
      })
    }

    $scope.__init__()
  
  })
  