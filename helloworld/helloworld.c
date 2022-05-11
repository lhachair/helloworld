
#define _GNU_SOURCE
#include <stdio.h>
#include <string.h>
#include <json-c/json.h>
#include "wrap-json.h"

#define AFB_BINDING_VERSION 3
#include <afb/afb-binding.h>


void hello (afb_req_t request)
{
    AFB_req_DEBUG(request, "hello world");
    afb_req_reply(request, NULL, NULL, "hello world");
}

const afb_verb_t verbs[] = {
    {.verb="hello",.session = AFB_SESSION_NONE, .callback=hello, .auth=NULL },
    {NULL}
};

const afb_binding_t afbBindingExport = {
    .api = "helloworld",
    .verbs = verbs
}