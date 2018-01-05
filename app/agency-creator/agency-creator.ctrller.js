angular.module('SLApp')
    .controller('AgencyCreatorCtrller', ['$scope', 'SLService','$location',
            function AgencyCreatorCtrller($scope, SLService, $location) {
                    console.log('init AgencyCreatorCtrller');
                    $scope.gradeMapper = {
                            '0':'PADAWAN',
                            '1':'JEDI',
                            '2':'MASTER'
                    }
                    $scope.gradeKeys = Object.keys($scope.gradeMapper)


                     $scope.addAgency = function () {
                            SLService.addAgency({
                                    'name' : $scope.addform.name,
                                    'description' : $scope.addform.description,
                                    'grade' : $scope.addform.grade,
                                    'tags': $scope.addform.tags})
                    }
            }]);