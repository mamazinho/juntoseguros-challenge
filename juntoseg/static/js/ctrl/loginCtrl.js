challenge.controller('LoginCtrl', function($scope, HttpFctr, $timeout){

  $scope.__init__ = function(){
    $scope.loginData = {
      'email': '',
      'password': '',
    }
  }

  $scope.login = () => {
    HttpFctr('login', 'POST', {data: $scope.loginData}).then((response) => {
      console.log(response)
      $scope.$emit('setToken', response)
      location = window.dashUrl
      $timeout(() => {
        $scope.goToDashboard()
      }, 2000)
    }).catch((error) => {
      console.log('Error >> ', error)
      alert(window.errorMessage)
    })
  }

  $scope.goToDashboard = () => {
    HttpFctr('dashboard', 'GET').then((response) => {
      console.log(response)
    }).catch((error) => {
      console.log('Error >> ', error)
      alert(window.errorMessage)
    })
  }

  $scope.__init__()

})
