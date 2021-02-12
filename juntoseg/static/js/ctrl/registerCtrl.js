challenge.controller('RegisterCtrl', function($scope, HttpFctr, $timeout){

  $scope.__init__ = function(){
    $scope.showCofirmModal = false
    $scope.myTokenConfirmation = ''
    $scope.seeToken = false
    $scope.registerData = {
      'email': '',
      'name': '',
      'password': '',
      'confirmPassword': ''
    }
  }
  
  $scope.register = () => {
    HttpFctr('register', 'POST', {data: $scope.registerData})
    .then((response) => {
      $scope.showCofirmModal = true
      $scope.myTokenConfirmation = response.token
    }).catch((error) => {
      console.log('Error >> ', error)
      alert(window.errorMessage)
    })
  }

  $scope.confirm = () => {
    HttpFctr('confirm-account', 'POST', {data: {token: $scope.myTokenConfirmation}})
    .then((response) => {
      console.log(response)
      $scope.showCofirmModal = false
      $scope.goToBase()
    }).catch((error) => {
      console.log('Error >> ', error)
      alert(window.errorMessage)
    })
  }

  $scope.goToBase = () => {
    $timeout(() => {
      HttpFctr('', 'GET')
    }, 2000)
  }

  $scope.__init__()

})
