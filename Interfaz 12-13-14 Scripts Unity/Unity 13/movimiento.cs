using System.Collections;
using System.Collections.Generic;
using UnityEngine;

[RequireComponent(typeof(CharacterController))]

public class movimiento : MonoBehaviour
{
    public float speed = 3.0F;
    public float rotateSpeed = 3.0F;
    public float jumpSpeed = 8.0F; // Jump speed
    public float gravity = 20.0F;   // Gravity force


    private Vector3 moveDirection = Vector3.zero;
    private CharacterController controller;


    void Start()
    {
        controller = GetComponent<CharacterController>();
    }


    void Update()
    {
        if (controller.isGrounded)
        {
            // Rotate the character based on horizontal input
            transform.Rotate(0, Input.GetAxis("Horizontal") * rotateSpeed, 0);


            // Move the character forward/backward
            moveDirection = transform.TransformDirection(Vector3.forward) * speed * Input.GetAxis("Vertical");


            // Check if the jump button (space bar) is pressed
            if (Input.GetButton("Jump"))
            {
                // Apply the jump speed to moveDirection.y
                moveDirection.y = jumpSpeed;
            }
        }

        // Apply gravity
        moveDirection.y -= gravity * Time.deltaTime;


        // Move the character
        controller.Move(moveDirection * Time.deltaTime);
    }
}
