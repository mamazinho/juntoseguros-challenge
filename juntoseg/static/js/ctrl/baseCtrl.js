challenge.controller('BaseCtrl', function($scope, $rootScope){

    $scope.__init__ = function(){
      $rootScope.active_tab = 'login'
      window.errorMessage = ''
      $scope.$on('changeTab', (event, data) => {
        $scope.active_tab = data
      })
    }
  
    $scope.__init__()
  
  })
  