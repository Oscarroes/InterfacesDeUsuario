using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class MovimientoPelota : MonoBehaviour
{
    public float moveSpeed = 5f; // Velocidad de movimiento de la pelota
    public float jumpForce = 10f; // Fuerza de salto de la pelota
    private bool isGrounded; // Indica si la pelota está en el suelo

    private Rigidbody rb;

    void Start()
    {
        rb = GetComponent<Rigidbody>();
    }

    void Update()
    {
        // Verificar si la barra espaciadora está siendo presionada y la pelota está en el suelo
        if (Input.GetKeyDown(KeyCode.Space) && isGrounded)
        {
            // Aplicar fuerza hacia arriba para simular el salto
            rb.AddForce(Vector3.up * jumpForce, ForceMode.Impulse);
            // Indicar que la pelota ya no está en el suelo
            isGrounded = false;
        }
    }

    void FixedUpdate()
    {
        // Input de los ejes horizontal y vertical
        float moveHorizontal = Input.GetAxis("Horizontal");
        float moveVertical = Input.GetAxis("Vertical");

        // Crear un vector de movimiento basado en la entrada de los ejes
        Vector3 movement = new Vector3(moveHorizontal, 0.0f, moveVertical);

        // Mover la pelota en la dirección especificada
        rb.AddForce(movement * moveSpeed);

        // Rotar la pelota según la dirección de movimiento
        if (movement != Vector3.zero)
        {
            Quaternion newRotation = Quaternion.LookRotation(movement);
            rb.rotation = Quaternion.Slerp(rb.rotation, newRotation, Time.fixedDeltaTime * moveSpeed);
        }
    }

    void OnCollisionEnter(Collision collision)
    {
        // Verificar si la pelota está en contacto con una superficie etiquetada como "Ground"
        if (collision.gameObject.CompareTag("Ground"))
        {
            // Indicar que la pelota está en el suelo
            isGrounded = true;
        }
    }
}
