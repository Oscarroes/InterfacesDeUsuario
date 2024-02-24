using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class triggerCollider : MonoBehaviour
{
    public Light spotlight; // Reference to the Spotlight component

    private void OnTriggerEnter(Collider other)
    {
        if (other.CompareTag("Personaje")) // Check if the object entering the trigger is the player
        {
            spotlight.enabled = true; // Turn on the spotlight
        }
    }

    private void OnTriggerExit(Collider other)
    {
        if (other.CompareTag("Personaje")) // Check if the object exiting the trigger is the player
        {
            spotlight.enabled = false; // Turn off the spotlight
        }
    }
}
