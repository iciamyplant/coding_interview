#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define TABLE_SIZE 100000



typedef struct      entry_t 
{
    char            *key; // le mot auquel on applique la hash table (par exemple le mot lasagne)
    char            *value; // valeur associée au mot (par exemple le nom d'un site)
    struct entry_t  *next;
}                   entry_t;

typedef struct
{
    entry_t         **entries;
}                   ht_t;



ht_t *ht_create(void) // create hash table
{    
    int i = 0;

    ht_t *hashtable = malloc(sizeof(ht_t) * 1); // allocate table
    hashtable->entries = malloc(sizeof(entry_t*) * TABLE_SIZE); // allocate table entries
    while (i < TABLE_SIZE) // set to NULL
    {
        hashtable->entries[i] = NULL;
        i++;
    }
    return (hashtable);
}

entry_t *ht_pair(const char *key, const char *value)
{
    entry_t *entry;

    entry = malloc(sizeof(entry_t) * 1); // allocate the entry
    entry->key = malloc(strlen(key) + 1);
    entry->value = malloc(strlen(value) + 1);
    strcpy(entry->key, key); // copy the key
    strcpy(entry->value, value); // copy the value
    entry->next = NULL; // next starts out null but may be set later on
    return (entry);
}

unsigned int hash_function(const char *key)
{
    int i = 0;
    unsigned long int value = 0;
    unsigned int key_len = strlen(key);

    while (i < key_len)
    {
        value = value * 37 + key[i]; // calcul
        i++;
    }
    value = value % TABLE_SIZE; // make sure : value >= 0 && value is <= TABLE_SIZE
    //printf("i = %d\n", i);
    return (value);
}

void ht_set(ht_t *hashtable, const char *key, const char *value)
{
    unsigned int    slot;
    entry_t         *entry;
    entry_t         *prev;
  
    slot = hash_function(key); // slot est l'index donné par la hash function
    entry = hashtable->entries[slot]; // try to look up an entry set
    if (entry == NULL) // no entry means slot empty, insert immediately
    {
        hashtable->entries[slot] = ht_pair(key, value);
        return;
    }
    //for collisions :
    while (entry != NULL) // si on tombe sur une case nulle ça veut dire notre key n'existe pas dans la table
    {
        if (strcmp(entry->key, key) == 0) // on est arrivé sur la key qu'on cherche
        {
            free(entry->value);
            entry->value = malloc(strlen(value) + 1);
            strcpy(entry->value, value);
            return;
        }
        prev = entry; // on parcourt la liste chaînée
        entry = prev->next; // on parcourt la liste chaînée
    }
    prev->next = ht_pair(key, value); // end of chain reached without a match, add new
}

char *ht_get(ht_t *hashtable, const char *key) // find the value quand on donne la key
{
    unsigned int    slot;

    slot = hash_function(key);
    entry_t *entry = hashtable->entries[slot]; // try to find a valid slot
    if (entry == NULL) // ça veut dire que notre key nest pas dans la hash table
        return NULL;
    while (entry != NULL) // walk through each entry in the slot, which could just be a single thing
    {
        if (strcmp(entry->key, key) == 0)
            return (entry->value); // ça veut dire on est bien sur notre key on peut retourner la valeur associée
        entry = entry->next; // sinon ça veut dire y a eu une collision on va a la suivante
    }
    return NULL; // reaching here means there were >= 1 entries but no key match
}

void ht_del(ht_t *hashtable, const char *key) // pour delete une key/value de ma hash table
{
    unsigned int    bucket;
    entry_t         *prev;
    int             idx = 0;
    
    bucket = hash_function(key);
    entry_t *entry = hashtable->entries[bucket]; // try to find a valid bucket
    if (entry == NULL) // no bucket means no entry
        return;
    while (entry != NULL) // walk through each entry until either the end is reached or a matching key is found
    {
        if (strcmp(entry->key, key) == 0) // check key
        {
            if (entry->next == NULL && idx == 0) // first item and no next entry
                hashtable->entries[bucket] = NULL;
            if (entry->next != NULL && idx == 0) // first item with a next entry
                hashtable->entries[bucket] = entry->next;
            if (entry->next == NULL && idx != 0)// last item
                prev->next = NULL;
            if (entry->next != NULL && idx != 0)// middle item
                prev->next = entry->next;
            // free the deleted entry
            free(entry->key);
            free(entry->value);
            free(entry);
            return;
        }
        prev = entry;
        entry = prev->next; // walk to next
        ++idx;
    }
}

int main(int argc, char **argv)
{
    const   char *key = "lasagne";
    ht_t    *ht = ht_create();

    ht_set(ht, "lasagne", "wbesite_nbr1");
    printf("Value associée à \"%s\" est : \"%s\"\n", key, ht_get(ht, key));
    ht_del(ht, key);
    printf("-------Après ht_del(ht, key)-------\n");
    printf("Value associée à \"%s\" est : \"%s\"\n", key, ht_get(ht, key));

    //printf("value = %d\n", hash_function(key));
    //printf("%s\n", key);
}