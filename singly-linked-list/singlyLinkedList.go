package main

import "fmt"

type Node struct {
	Value int
	Next  *Node
}

// Retturns pointers to the initialized memory for root node
var head = new(Node)

func (node *Node) addNode(value int) {
	if node == nil {
		head = node.addInitialNode(value)
	}
}

// add the first node
func (node *Node) addInitialNode(value int) *Node {
	addedNode := Node{Value: value, Next: nil}
	node = &addedNode
	return node
}

// Add the node at the begining of the list
func (node *Node) pushNode(value int) {
	var newNode Node
	newNode.Value = value
	newNode.Next = *&head
	head = &newNode
}

// Add the node at the end of the list
func (node *Node) appendNode(value int) {
	isNextNodePresent := true
	for isNextNodePresent == true {
		if node.Next != nil {
			node = node.Next
		} else {
			newNode := Node{Value: value, Next: nil}
			node.Next = &newNode
			isNextNodePresent = false
		}
	}
}

// Travel to each and every node and print its value
func (node *Node) traverse() {
	if node == nil {
		fmt.Println("Empty List!")
	}

	for node != nil {
		fmt.Print("->", *node)
		node = node.Next
	}
	fmt.Println()
}

// Search if the item is present in the list.
func (node *Node) searchItem(value int) bool {
	if node == nil {
		return false
	}
	if value == node.Value {
		return true
	}
	if node.Next == nil {
		return false
	}
	return node.Next.searchItem(value)
}

// Print the sile of the list
func (node *Node) listLength() int {
	if node == nil {
		return 0
	}
	size := 1
	for node.Next != nil {
		size++
		node = node.Next
	}
	return size
}

// Adds the node after the given position
func (node *Node) addInMiddle(value int, position int) {
	currentPos := 1
	for node.Next != nil {
		if position == currentPos {
			var newNode Node
			newNode.Value = value
			newNode.Next = node.Next
			node.Next = &newNode
		}
		currentPos++
		node = node.Next
	}
}

// func (node *Node) deleteNode(value int) int {

// 	temp := node
// 	if node.listLength() == 0 {
// 		fmt.Println("Cannot delete empty list.")
// 		return 0
// 	}

// 	if node.Value == value {
// 		head = node.Next
// 		return 0
// 	}

// 	for node.Next != nil {
// 		if node.Value == value {
// 			node = temp
// 			node.Next = temp.Next.Next
// 			return 0
// 		}
// 		node = node.Next
// 		temp = node
// 	}

// 	return 0
// }

func main() {
	head = nil
	head.addNode(5)
	head.pushNode(3)
	head.appendNode(4)
	head.appendNode(7)
	head.addInMiddle(10, 2)

	head.traverse()

	// head.deleteNode(5)

	head.traverse()
}
