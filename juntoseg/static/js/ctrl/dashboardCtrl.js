
challenge.controller('DashboardCtrl', function($scope, HttpFctr){

    $scope.__init__ = function(){
        $scope.profile = {}
        $scope.users = []
        $scope.dashboard()
    }

    $scope.dashboard = () => {
        HttpFctr('dashboard', 'GET').then((response) => {
            $scope.profile = response.profile
            $scope.users = response.users
        }).catch((error) => {
        console.log('Error >> ', error)
            alert(window.errorMessage)
        })
    }

    $scope.__init__()

})
