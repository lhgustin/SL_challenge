angular.module('SLApp')
    .controller('AgencyCreatorCtrller', ['$scope', 'SLService','$location',
            function AgencyCreatorCtrller($scope, SLService, $location) {
                    console.log('init AgencyCreatorCtrller');
                    $scope.gradeMapper = SLService.gradeMapper
                    $scope.gradeKeys = Object.keys($scope.gradeMapper)
                    $scope.addform = {} // must be object first
                    $scope.addform.grade = '0' // default, must be string as above

                     $scope.addAgency = function () {
                            SLService.addAgency({
                                    'name' : $scope.addform.name,
                                    'description' : $scope.addform.description,
                                    'grade' : $scope.addform.grade,
                                    'tags': $scope.addform.tags})
                    }
            }]);