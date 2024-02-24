using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class triggerMoneda1 : MonoBehaviour
{
    private void OnTriggerEnter(Collider other)
    {
        Debug.Log("Alguien me ha tocado");
        Destroy(gameObject);
    }
}
