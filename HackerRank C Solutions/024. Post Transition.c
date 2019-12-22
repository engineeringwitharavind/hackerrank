/* Post Transition in C */

#include <stdio.h>
#include <stdlib.h>
#include <string.h> //Added
#define MAX_STRING_LENGTH 6

struct package
{
    char* id;
    int weight;
    struct package* next;   //Added
};
typedef struct package package;

struct post_office
{
    int min_weight;
    int max_weight;
    package* packagesHead;  //Added
    package* packagesTail;  //Added
	//package* packages;    //Removed
    int packages_count;
};
typedef struct post_office post_office;

struct town
{
    char* name;
    post_office* offices;
    int offices_count;
};
typedef struct town town;

void func_InsertPackages(post_office* office){  //Added
    if(office->packagesHead==NULL){
        office->packagesHead = (package*)malloc(sizeof(package));
        office->packagesTail = office->packagesHead;
    }
    else{
        office->packagesTail->next = (package*)malloc(sizeof(package));
        office->packagesTail = office->packagesTail->next;
    }
    office->packagesTail->next = NULL;
    office->packagesTail->id = malloc(sizeof(char) * MAX_STRING_LENGTH);
    scanf("%s", office->packagesTail->id);
    scanf("%d", &office->packagesTail->weight);
    return;
}

void func_AppendPackage(package** Head, package** Tail, package* node){ //Added
    if((*Head)==NULL){
        *Head = node;
        *Tail = node;
    }
    else{
        (*Tail)->next = node;
        *Tail = node;
    }
}

void func_RemovePackage(package** Head,package** Tail,package* prev,package* current){  //Added
    if((*Head)==prev && prev==current)
        *Head = current->next;
    else if((*Tail)==current)
        (*Tail) = prev;
    prev->next=current->next;
}

void print_all_packages(town t) {
    printf("%s:\n",t.name);
    for(int i=0; i<t.offices_count; i++){
        printf("\t%d:\n",i);
        package* node = t.offices[i].packagesHead;
        while(node!=NULL){
            printf("\t\t%s\n",node->id);
            node = node->next;
        }
    }
}

void send_all_acceptable_packages(town* source, int source_office_index, town* target, int target_office_index) {
    post_office* sourceOffice = source->offices+source_office_index;
    post_office* targetOffice = target->offices+target_office_index;

    package* travelS = sourceOffice->packagesHead;
    package* tempPreviousS = travelS;
    package* tempDeleteS = travelS;
    package** sourceHead = &sourceOffice->packagesHead;
    package** sourceTail = &sourceOffice->packagesTail;
    package** targetHead = &targetOffice->packagesHead;
    package** targetTail = &targetOffice->packagesTail;

    while(travelS!=NULL){
        if((travelS->weight>=targetOffice->min_weight) && (travelS->weight<=targetOffice->max_weight)){
            func_AppendPackage(targetHead,targetTail,travelS);
            func_RemovePackage(sourceHead,sourceTail,tempPreviousS,travelS);
            travelS = travelS->next;
            (*targetTail)->next = NULL;
            targetOffice->packages_count++;
            sourceOffice->packages_count--;
        }
        else{
            tempPreviousS = travelS;
            travelS = travelS->next;
        }
    }
}

town town_with_most_packages(town* towns, int towns_count) {
    int twmpi = 0; //Town With Most Packages Index
    int mpnt = 0; //Maximum Packages Number of a Twon
    int pnt = 0; //Packages Number of a Town
    for(int i=0; i<towns_count; i++,pnt=0){
        for(int j=0; j<towns[i].offices_count; j++)
            pnt+= towns[i].offices[j].packages_count;
        if(pnt>mpnt){
            mpnt = pnt;
            twmpi = i;
        }
    }
    return towns[twmpi];
}

town* find_town(town* towns, int towns_count, char* name) {
    int townIndex = 0;
    for(int i=0; i<towns_count; i++)
        if(strcmp(towns[i].name,name)==0){
            townIndex = i;
            break;
        }
    return &towns[townIndex];
}

int main()
{
    int towns_count;
    scanf("%d", &towns_count);
    town* towns = malloc(sizeof(town)*towns_count);
    for (int i = 0; i < towns_count; i++) {
        towns[i].name = malloc(sizeof(char) * MAX_STRING_LENGTH);
        scanf("%s", towns[i].name);
        scanf("%d", &towns[i].offices_count);
        towns[i].offices = calloc(towns[i].offices_count,sizeof(post_office));
        for (int j = 0; j < towns[i].offices_count; j++) {
            scanf("%d%d%d", &towns[i].offices[j].packages_count, &towns[i].offices[j].min_weight, &towns[i].offices[j].max_weight);
            //towns[i].offices[j].packages = malloc(sizeof(package)*towns[i].offices[j].packages_count);    //Removed
            for (int k = 0; k < towns[i].offices[j].packages_count; k++) {
                func_InsertPackages(&towns[i].offices[j]);  //Added
                /*towns[i].offices[j].packages[k].id = malloc(sizeof(char) * MAX_STRING_LENGTH);
                scanf("%s", towns[i].offices[j].packages[k].id);
                scanf("%d", &towns[i].offices[j].packages[k].weight);*/ //Removed
            }
        }
    }

    int queries;
    scanf("%d", &queries);
    char town_name[MAX_STRING_LENGTH];
    while (queries--) {
        int type;
        scanf("%d", &type);
        switch (type) {
        case 1:
            scanf("%s", town_name);
            town* t = find_town(towns, towns_count, town_name);
            print_all_packages(*t);
            break;
        case 2:
            scanf("%s", town_name);
            town* source = find_town(towns, towns_count, town_name);
            int source_index;
            scanf("%d", &source_index);
            scanf("%s", town_name);
            town* target = find_town(towns, towns_count, town_name);
            int target_index;
            scanf("%d", &target_index);
            send_all_acceptable_packages(source, source_index, target, target_index);
            break;
        case 3:
            printf("Town with the most number of packages is %s\n", town_with_most_packages(towns, towns_count).name);
            break;
        }
    }
    return 0;
}
