var myApp = angular.module('myApp', []);

// getting data from a service
myApp.factory('Data', function(){
	return{message: "I'm data from a service"}

});

// Simple controller setup
function FirstCtrl($scope, Data ) {
//	$scope.data = {message: "Hello"};
	$scope.data = Data;

}

function SecondCtrl($scope, Data) {
	//$scope.data = {message: "Hello"};
	$scope.data = Data;
	$scope.reversedMessage = function(message){
		return message.split("").reverse().join("");
	}
}

function HelloController($scope) {
	$scope.greeting = { text: "Hello" };
}