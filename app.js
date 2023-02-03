(function(){
    'use strict';

    angular.module('myFirstApp',[])
    
    .controller('MyFirstController', function ($scope){
        $scope.name ="tao"

        $scope.sayHello = function () {
            return("hello tao")
        }
    });

})();