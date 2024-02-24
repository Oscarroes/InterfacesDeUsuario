using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class TriggerLuces : MonoBehaviour
{
    public Light spotlight; // Reference to the Spotlight component
    public Light pointlight; // Reference to the pointlight component

    private void OnTriggerEnter(Collider other)
    {
        if (other.CompareTag("personaje")) // Check if the object entering the trigger is the player
        {
            spotlight.enabled = true; // Turn on the spotlight
            pointlight.enabled = false; // Turn off the pointlight
        }
    }

    private void OnTriggerExit(Collider other)
    {
        if (other.CompareTag("personaje")) // Check if the object exiting the trigger is the player
        {
            spotlight.enabled = false; // Turn off the spotlight
            pointlight.enabled = true; // Turn on the pointlight
        }
    }
}
