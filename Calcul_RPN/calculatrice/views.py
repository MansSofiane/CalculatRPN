from django.shortcuts import render
from rest_framework.decorators import api_view
from django.http import HttpResponse, JsonResponse
import jsonpickle
from rest_framework import status
from rest_framework.response import Response
from .models import Stack,operation


@api_view(['GET', 'POST'])
def operation(request,fk):
    if  request.method == 'GET':
        pile = operation.object.filter(stack=fk)
        piles = []
        piles.append({"number":pile.number, "stack":pile.stack})
        return HttpResponse(jsonpickle.encode(piles, unpicklable=False), content_type="application/json")
    if request.method == 'POST':
        number = request.data['number']
        stack = request.data['stack']
        try:
            pile = operation(
                number = number,
                stack = stack
            )
            pile.save()
        except Exception as e:
            return JsonResponse({'message': 'error occured'}, status=status.HTTP_404_NOT_FOUND)
        return JsonResponse({'message': 'Added successfully'}, status=status.HTTP_200_OK)


@api_view(['GET', 'POST'])
def push(request):
    if  request.method == 'GET':
        pile = Stack.objects.all()
        piles = []
        for i in pile:
            piles.append({"name":i.Name})
        return HttpResponse(jsonpickle.encode(piles, unpicklable=False), content_type="application/json")
    if request.method == 'POST':
        name = request.data['Name']
        try:
            pile = Stack(
                Name = name
            )
            pile.save()
        except Exception as e:
            return JsonResponse({'message': 'error occured'}, status=status.HTTP_404_NOT_FOUND)
        return JsonResponse({'message': 'Added successfully'}, status=status.HTTP_200_OK)

@api_view(['GET', 'PUT', 'DELETE'])
def Delet(request,pk):
    pile = Stack.objects.get(pk=pk)
    if  request.method == 'DELETE':
        pile.delete()
        return JsonResponse({'message': 'deleted successfully'}, status=status.HTTP_200_OK)
    if  request.method == 'GET':
        piles = []
        piles.append({"name":pile.Name})
        return HttpResponse(jsonpickle.encode(piles, unpicklable=False), content_type="application/json")


def drop(self):
    "Drop the last inserted item out of the stack"
    self.stack.pop()
def plus(self, digit1, digit2):
    "Add two digits"
    return [digit1 + digit2]
def minus(self, digit1, digit2):
    "Substract two digits"
    return [digit2 - digit1]
def multiply(self, digit1, digit2):
    "Multiply two digits"
    return [digit1 * digit2]
def divide(self, digit1, digit2):
    "Divide two digits"
    try:
        return [digit2 / digit1]
    except NameError as err:
        print(err)